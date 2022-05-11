import tweepy
import json
import couchdb
from locate_postcode import postcode


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

# define our keyword, for example KEYWORD='good',KEYWORD='good OR bad'
KEYWORD = ''
# the city we want to search, for example PLACE = 'sydney' or PLACE = 'melbourne'
PLACE= 'melbourne'
# file containing about 20 searching points covering most areas in greater melbourne area(only)
# e.g. mel cbd = "-37.818219,144.965817,4km"
# note that this file will be only used when keyword is null
RANGE_FILE = 'havesting_points_mel.json'
# max number of tweets we want to retreive in every search
SEARCH_NUM = 10000
# if we only need tweets with coordinte to store in db
ONLY_SAVE_TWEETS_WITH_GEO = True
#replace this url on MRC
login_info = "http://user:pass@0.0.0.0:5984"
server = couchdb.Server(login_info)
db_name = 'twitter'
try:
    twitter_db = server[db_name]
except couchdb.http.ResourceNotFound:
    print('db not on server, please set up couchdb first')
    exit()

#to see if we are authenticated in tweepy api
try:
    api.verify_credentials()
    print('Authentication OK')
except:
    print('Error during authentication')

def save_data_in_db(db, tweet_list):
    num = 0
    if len(tweet_list) > 0:
        for tweet in tweet_list:
            if tweet["id"] not in db:
                try:
                    db[tweet["id"]] = tweet
                    num += 1
                except couchdb.http.ResourceConflict:
                    continue
        print(num,'new tweets written in db',db)
    else:
        print('no tweets to write')
    

def search_tweets_by_geocode(keyword, geoc, limit):
    result_list = []
    query='{}'.format(keyword)
    request_limit = 10
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
                post_code = postcode(this_tweet['geo']['coordinates'])
                #print(post_code)
                js = {'created_at':this_tweet['created_at'],
                      'id':str(this_tweet['id']),
                      'text':this_tweet['text'],
                      'geo':this_tweet['geo'],
                      'lang':this_tweet['lang'],
                      'city':PLACE,
                      'postcode':post_code}
                #print(js)
                #print('\n-----------------\n')
                result_list.append(js)
            searched += 1
        print('searched:',searched,'tweets')
        print('has geo:',hasgeo,'tweets')        
    except tweepy.RateLimitError:
        print('Hit Rate Limit. Sleep for 15min')
        time.sleep(15*60)
    return result_list

def search_tweets_by_place(keyword, place, limit):
    result_list = []
    places = api.search_geo(query=place, granularity="city")
    place_id = places[0].id    
    query='{}'.format(keyword)
    request_limit = 10
    if limit >= 100:
        request_limit = 100
    query='{} place:{}'.format(keyword, place_id)
    try:
        tweets = tweepy.Cursor(api.search_tweets,q=query,count=request_limit).items(limit)
        searched = 0
        hasgeo = 0
        for t in tweets:
            this_tweet = t._json
            js = {'created_at':this_tweet['created_at'],
                  'id':str(this_tweet['id']),
                  'text':this_tweet['text'],
                  'geo':this_tweet['geo'],
                  'lang':this_tweet['lang'],
                  'city':PLACE}            
            if this_tweet['geo']!=None:
                hasgeo += 1
            if ONLY_SAVE_TWEETS_WITH_GEO:
                if this_tweet['geo']!=None:
                    #print(js)
                    #print('\n-----------------\n')
                    result_list.append(js)
            else:
                #print(js)
                #print('\n-----------------\n')                
                result_list.append(js)
            searched += 1
        print('searched:',searched,'tweets')
        print('has geo:',hasgeo,'tweets')        
    except tweepy.RateLimitError:
        print('Hit Rate Limit. Sleep for 15min')
        time.sleep(15*60)
    return result_list    


def main():
    if KEYWORD == '':
        with open(RANGE_FILE, 'r',encoding='utf-8') as f:
            p = json.load(f)
            points = p['points']
        for point in points:
            geoc = point['coordinate']+','+point['radius']
            print('searching:',geoc)    
            tweets_list = search_tweets_by_geocode(KEYWORD,geoc,SEARCH_NUM)
            save_data_in_db(twitter_db, tweets_list)
            #print('wait 1 min and search the next point')
            #time.sleep(1*60)         
    else:
        print('searching in:',PLACE,'\nkeyword:',KEYWORD)
        tweets_list = search_tweets_by_place(KEYWORD,PLACE,SEARCH_NUM)
        save_data_in_db(twitter_db, tweets_list)
            
if __name__ == "__main__":
    main()
