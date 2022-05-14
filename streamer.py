#****************************
# 2022 COMP90024 Cluster and Cloud Computing Assignment 2 TEAM 2
#****************************

import tweepy
import json
import couchdb
import time
from DB_Constants import *
from UtilityFunctions import *

# passing in tokens and url
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


class MyStreamListener(tweepy.Stream):
    """override tweepy.Stream to add logic"""
    def __init__(self, start_time,time_limit,consumer_key,consumer_secret,
                 access_token,access_token_secret,db_name):
        self.start_time = start_time
        self.limit = time_limit
        # try connecting to couchDB
        try:
            self.twitter_db = server[db_name]
        except couchdb.http.ResourceNotFound:
            print('db not on server, please set up couchdb first')
            exit()        
        super(MyStreamListener, self).__init__(consumer_key=consumer_key,consumer_secret=consumer_secret,
                                   access_token=access_token,access_token_secret=access_token_secret)
        
    def on_status(self, status):
        print(status.text)

    #  define how to process each tweet captured
    def on_data(self, data):
        this_tweet = json.loads(data)
        if len(this_tweet) != 1:
            # the data is a captured tweet, process it and store in db
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
            # pre-defined stream time has passed, stop streaming 
            print('Streaming finish')
            self.running = False             
      

    def on_error(self,status):
        print(status)
        if status =='420':
            time.sleep(20*60)    

def save_tweet_in_db(db,tweet_dict):
    """save a tweet json in db"""
    if tweet_dict['doc']['id'] not in db:
        db[tweet_dict['doc']['id']] = tweet_dict
        print('saved 1 tweet with id', tweet_dict['doc']['id'])


for topic in topics:
    # start time is now
    start_time= time.time()
    # specify db_name for this topic
    db_name = topic[0]+'_stream'
    stream = MyStreamListener(start_time,STREAM_TIME,consumer_key,consumer_secret,
                                   access_token,access_token_secret,db_name = db_name)
    if len(topic) <= 1:
        # there are no keyword for this topic, stream with no keyword but with location detail
        stream.filter(track='',locations=MEL)
    else:
        # get keywords and pass them to streamer along with loation
        keywords = generate_keywords(topic)
        stream.filter(track= keywords, locations=MEL)


