import tweepy
import json
import couchdb
from locate_postcode import postcode
import time

with open('api_tokens.json', 'r',encoding='utf-8') as f:
    keys = json.load(f)
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']
bearer_token = keys['bearer_token']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# define our keyword, for example KEYWORD=['good'] or KEYWORD=['good','bad']
KEYWORD = ['covid','pandemic']
# how many seconds will the streaming go, we recommend longer time if only geo-coded tweets is needed
STREAM_TIME = 10
# if we only need tweets with coordinte to store in db
ONLY_SAVE_TWEETS_WITH_GEO = False

login_info = "http://user:pass@0.0.0.0:5984"
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
        js = {'created_at':this_tweet['created_at'],
              'id':str(this_tweet['id']),
              'text':this_tweet['text'],
              'geo':this_tweet['geo'],
              'lang':this_tweet['lang']}   
        if ONLY_SAVE_TWEETS_WITH_GEO:
            if js['geo']!= None:
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
    if tweet_dict['id'] not in db:
        db[tweet_dict['id']] = tweet_dict
        print('saved 1 tweet with id', tweet_dict['id'])

# bounding box for Australia and major cities in AU
AUS = [113.62,-44.1,153.14,-10.75]
MEL = [144.7092,-37.9803,145.2489,-37.6339]
SYD = [150.83,-33.9486,151.2917,-33.8167]
PER = [115.6325,-32.5417,116.0558,-31.6625]
BNE = [153.7031,27.7942,153.3964,-27.1439]
ADL = [153.7031,27.7942,153.3964,-27.1439]
start_time= time.time()
stream = MyStreamListener(start_time,STREAM_TIME,consumer_key,consumer_secret,
                                   access_token,access_token_secret,db_name = 'stream')

stream.filter(track=KEYWORD,locations=MEL)


