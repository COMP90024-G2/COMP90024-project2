
from Large_Melbourne_Twitter_Process import *
from ClassObjects import *
from Constants import *
from UtilityFunctions import *
from DataAnalysis import *

import couchdb

username = "admin"
password = "admin"
host = "172.26.130.73"
port = "5984"

def connect_to_couch_db_server(host, port, username, password):
    secure_remote_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return secure_remote_server

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

def read_from_db(database_name, server):
    database = connect_to_database(database_name, server)
    rows = database.view('_all_docs', include_docs=True)
    return [row['doc'] for row in rows]

def load_tweet_from_db(melb, tweet_lst):
    for item in tweet_lst:
        tweet = Tweet(item)
        locate_tweet_to_Area(tweet, melb)

def main():

    print("Starting")
    
    server = connect_to_couch_db_server(host, port, username, password)

    lang_aurin = read_from_db('aurin_lang', server)
    income_aurin = read_from_db('aurin_income', server)
    health_aurin = read_from_db('aurin_health', server)

    employment_keywords = generate_keywords(TOPICS[1])
    health_keywords = generate_keywords(TOPICS[2])
    large_melb_data = process_twitter_data(GEOFILE, LARGE_TWITTER, use_limit= True)

    extract_aurin_language(large_melb_data, lang_aurin)
    extract_aurin_income(large_melb_data, income_aurin)
    extract_aurin_health(large_melb_data, health_aurin)

    new_melb_data = initialize_melb_area(GEOFILE)

    load_tweet_from_db(large_melb_data, read_from_db('diversity_search', server))
    load_tweet_from_db(large_melb_data, read_from_db('employment_search', server))
    load_tweet_from_db(large_melb_data, read_from_db('health_search', server))    

    count_languages(large_melb_data)
    general_sentiment_analysis(large_melb_data)
    topic_sentiment_analysis(large_melb_data, employment_keywords, health_keywords)

    load_tweet_from_db(new_melb_data, read_from_db('diversity_stream', server))
    load_tweet_from_db(new_melb_data, read_from_db('employment_stream', server))

    topic_sentiment_analysis(new_melb_data, employment_keywords, health_keywords)

    load_tweet_from_db(new_melb_data, read_from_db('health_stream', server))

    topic_sentiment_analysis(new_melb_data, employment_keywords, health_keywords)

    count_languages(new_melb_data)
    
    general_sentiment_analysis(new_melb_data)
    
    hist_output = condense_output(large_melb_data)
    new_output = condense_output(new_melb_data)

    result = {"historical_analysis": hist_output, "new_analysis": new_output}

    resultdb = connect_to_database('output', server)
    rows = resultdb.view('_all_docs', include_docs=True)
    for row in rows:
        resultdb.delete(row['doc'])

    resultdb.save(result)

if __name__ == "__main__":
    main()


