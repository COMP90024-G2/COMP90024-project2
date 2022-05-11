import tweepy
import json
import couchdb
import time
from DB_Constants import *
from UtilityFunctions import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

topics = TOPICS

server = couchdb.Server(login_info)

#to see if we are authenticated in tweepy api
try:
    api.verify_credentials()
    print('Authentication OK')
except:
    print('Error during authentication')
    exit()

#override tweepy.Stream to add logic to on_status
class MyStreamListener(tweepy.Stream):
    def __init__(self, start_time,time_limit,consumer_key,consumer_secret,
                 access_token,access_token_secret,db_name):
        self.start_time = start_time
        self.limit = time_limit
        try:
            self.twitter_db = server[db_name]
        except couchdb.http.ResourceNotFound:
            print('db not on server, please set up couchdb first')
            exit()        
        super(MyStreamListener, self).__init__(consumer_key=consumer_key,consumer_secret=consumer_secret,
                                   access_token=access_token,access_token_secret=access_token_secret)
        
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        this_tweet = json.loads(data)
        #print(this_tweet,'\n------------------------------\n')
        if len(this_tweet) != 1:
            js = {"doc":{'created_at':this_tweet['created_at'],
                  'id':str(this_tweet['id']),
                  'text':this_tweet['text'],
                  'geo':{'coordinates':this_tweet['geo']},
                  'lang':this_tweet['lang']}}
            if ONLY_SAVE_TWEETS_WITH_GEO:
                if js['doc']['geo']!= None:
                    save_tweet_in_db(self.twitter_db,js)
                    #print(js)
                    #print('\n-----------------\n')
            else:
                save_tweet_in_db(self.twitter_db,js)
                #print(js)
                #print('\n-----------------\n')
        if (time.time()-self.start_time) > self.limit:
            print('Streaming finish')
            self.running = False             
      

    def on_error(self,status):
        print(status)
        if status =='420':
            time.sleep(20*60)    

def save_tweet_in_db(db,tweet_dict):
    if tweet_dict['doc']['id'] not in db:
        db[tweet_dict['doc']['id']] = tweet_dict
        print('saved 1 tweet with id', tweet_dict['doc']['id'])


for topic in topics:
    start_time= time.time()
    stream = MyStreamListener(start_time,STREAM_TIME,consumer_key,consumer_secret,
                                   access_token,access_token_secret,db_name = topic[0])
    if len(topic) <= 1:
        stream.filter(track='',locations=MEL)
    else:
        keywords = generate_keywords(topic)
        stream.filter(track= keywords, locations=MEL)


