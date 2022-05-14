#****************************
# 2022 COMP90024 Cluster and Cloud Computing Assignment 2 TEAM 2
#****************************

#DB and harvester constants

# Twitter API tokens
consumer_key = 'Oex1lHl5lDIw8TBJLg7hRWFjR'
consumer_secret = 'TNgrwsyEgPplQRHzLnjvKDE4w3eYBmhRbfbpJ5XvKllFaIgSSo'
access_token = '1514779005136023555-YLaKExiNIH6Kb2Za5hfFp5wgqc2wW4'
access_token_secret = 'c4dpN7xWkG9AQbRhyiUe9MePnjCMw7YD2G2r4bqDcnnrx'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANERbgEAAAAAHRe2CAGQuHCPLr19lgkFpz40wZ8%3DapZErVyfN7ppwelxsWVACwyXzdF15pvQCHMJWoyYoPTyvtHINP'

# couchDB url
login_info = "http://admin:admin@172.26.130.73:5984"

# if we want streamer/searcher to save tweets with coordinates only
ONLY_SAVE_TWEETS_WITH_GEO = False
# the streaming time for streamer
STREAM_TIME = 60
# define the keywords for topic 'EMPLOYMENT'
EMPLOYMENT = ["employment","job", "occupation", "income", "pay"]
# define the keywords for topic 'HEALTH'
HEALTH = ["health", "hospital","sick","unwell","doctor", "medicine", "drug"]
# the 3 topics we want to investigate in this project
TOPICS = [['diversity'], EMPLOYMENT, HEALTH]

# bounding box for Australia and major cities in AU
AUS = [113.62,-44.1,153.14,-10.75]
MEL = [144.7092,-37.9803,145.2489,-37.6339]
SYD = [150.83,-33.9486,151.2917,-33.8167]
PER = [115.6325,-32.5417,116.0558,-31.6625]
BNE = [153.7031,27.7942,153.3964,-27.1439]
ADL = [153.7031,27.7942,153.3964,-27.1439]