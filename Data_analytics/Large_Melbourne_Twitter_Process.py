# Large melbourne twitter analysis

from Constants import *
from ClassObjects import *
from UtilityFunctions import *
from DataAnalysis import *
import json
import mmap

def process_twitter_data(geo_file, twitter_file, use_limit = False):

    melb_city = initialize_melb_area(geo_file)

    with open(twitter_file,"rb") as f:       
        mm = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_READ)
        i = 0
        for line in iter(mm.readline, b""):

            i += 1

            if i == 1:
                data = json.loads(line.decode('utf-8')[:END_OF_LINE_START]+"]}")
                limit = data['total_rows']
                continue
            
            else:
                if use_limit == True:
                    if i <= READ_LIMIT:
                        try:
                            tweet = Tweet(json.loads(line.decode('utf-8')[:END_OF_LINE_BODY]))
                            if tweet.coords:
                                locate_tweet_to_Area(tweet, melb_city) 
                        except Exception as e:
                            print(e, " at entry:", line)
                            continue
                    else:
                        break 

                else:
                    if i < limit:
                        try:
                            tweet = Tweet(json.loads(line.decode('utf-8')[:END_OF_LINE_BODY]))
                            if tweet.coords:
                                locate_tweet_to_Area(tweet, melb_city) 
                        except Exception as e:
                            print(e, " at entry:", line)
                            continue
                    elif i == limit:
                        try:
                            tweet = Tweet(json.loads(line.decode('utf-8')[:END_OF_LINE_END]))
                            if tweet.coords:
                                locate_tweet_to_Area(tweet, melb_city)
                        except Exception as e:
                            print(e, " at entry:", line)
                            break     
                        break
                    else:
                        break
            
    return melb_city


