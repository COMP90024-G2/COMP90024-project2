import tweepy
import json
import couchdb
from DB_Constants import *
from UtilityFunctions import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

topics = TOPICS

server = couchdb.Server(login_info)
# file containing about 20 searching points covering most areas in greater melbourne area(only)
# e.g. mel cbd = "-37.818219,144.965817,4km"
# note that this file will be only used when keyword is null
RANGE_FILE = 'havesting_points_mel.json'
#to see if we are authenticated in tweepy api
try:
    api.verify_credentials()
    print('Authentication OK')
except:
    print('Error during authentication')
    exit()

def search_tweets_by_geocode(keyword, geoc, limit, db_name):
    result_list = []
    query='{}'.format(keyword)
    request_limit = 10
    try:
        twitter_db = server[db_name]
    except couchdb.http.ResourceNotFound:
        print('db not on server, please set up couchdb first')
        exit()        
    if limit >= 100:
        request_limit = 100
    try:
        tweets = tweepy.Cursor(api.search_tweets,q=query,geocode=geoc,count=request_limit).items(limit)
        searched = 0
        hasgeo = 0
        for t in tweets:
            this_tweet = t._json
            if this_tweet['geo']!=None:
                hasgeo += 1
            js = {"doc":{'created_at':this_tweet['created_at'],
                  'id':str(this_tweet['id']),
                  'text':this_tweet['text'],
                  'geo':{'coordinates':this_tweet['geo']},
                  'lang':this_tweet['lang']}}
            if ONLY_SAVE_TWEETS_WITH_GEO:
                if js['doc']['geo']!= None:
                    save_tweet_in_db(twitter_db,js)
                    #print(js)
                    #print('\n-----------------\n')
            else:
                save_tweet_in_db(twitter_db,js)
                #print(js)
                #print('\n-----------------\n')
            searched += 1
        print('searched:',searched,'tweets')
        print('has geo:',hasgeo,'tweets')        
    except tweepy.RateLimitError:
        print('Hit Rate Limit. Sleep for 15min')
        time.sleep(15*60) 

def search_tweets_by_place(keyword, place, limit, db_name):
    places = api.search_geo(query=place, granularity="city")
    place_id = places[0].id       
    query='{} place:{}'.format(keyword, place_id)
    request_limit = 10
    try:
        twitter_db = server[db_name]
    except couchdb.http.ResourceNotFound:
        print('db not on server, please set up couchdb first')
        exit()        
    if limit >= 100:
        request_limit = 100
    try:
        tweets = tweepy.Cursor(api.search_tweets,q=query,count=request_limit).items(limit)
        searched = 0
        hasgeo = 0
        for t in tweets:
            this_tweet = t._json
            if this_tweet['geo']!=None:
                hasgeo += 1
            js = {"doc":{'created_at':this_tweet['created_at'],
                  'id':str(this_tweet['id']),
                  'text':this_tweet['text'],
                  'geo':{'coordinates':this_tweet['geo']},
                  'lang':this_tweet['lang']}}
            if ONLY_SAVE_TWEETS_WITH_GEO:
                if js['doc']['geo']!= None:
                    save_tweet_in_db(twitter_db,js)
                    #print(js)
                    #print('\n-----------------\n')
            else:
                save_tweet_in_db(twitter_db,js)
                #print(js)
                #print('\n-----------------\n')
            searched += 1
        print('searched:',searched,'tweets')
        print('has geo:',hasgeo,'tweets')        
    except tweepy.RateLimitError:
        print('Hit Rate Limit. Sleep for 15min')
        time.sleep(15*60) 

def save_tweet_in_db(db,tweet_dict):
    if tweet_dict['doc']['id'] not in db:
        db[tweet_dict['doc']['id']] = tweet_dict
        print('saved 1 tweet with id', tweet_dict['doc']['id'])

def get_keyword(topic):
    if topic == 'diversity':
        keyword = ''
    elif topic == 'employment':
        keyword = 'job OR occupation OR income'
    elif topic == 'health':
        keyword = 'hospital OR sick OR drug'
    else:
        return topic
    return keyword
    

keyword = ''
for top in topics:
    topic  = top[0]
    keyword = get_keyword(topic)
    print('searching:',keyword)
    db_name = topic + "_search"
    if keyword == '':
        with open(RANGE_FILE, 'r',encoding='utf-8') as f:
            p = json.load(f)
            points = p['points']
        for point in points:
            geoc = point['coordinate']+','+point['radius']
            print('searching:',geoc)    
            search_tweets_by_geocode(keyword,geoc,10000,db_name)
            #print('wait 1 min and search the next point')
            #time.sleep(1*60)  
    else:
        search_tweets_by_place(keyword,'melbourne',10000,db_name)


