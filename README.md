# Twitter Harvester

## General info
The Twitter harvester is developed in Python language. The [Twitter API](https://developer.twitter.com/en/docs/platform-overview) supports programmatic access to Twitter in a fast and advanced way. In this project, we implemented two main methods to harvest tweets with regards to the topic we were concerned, which exploit the Streaming API and Searching API respectively. Both APIs provide keyword retrieval, which allows us to extract relevant tweets. [Tweepy](https://docs.tweepy.org/en/stable/api.html) is a specialized module for working with the Twitter API in Python.


## Getting Started
The application `Searcher.py` and `Streamer.py` make use of Twitter's Search and Stream API and stores the extracted tweets in CouchDB. The API tokens and some other constants (keywords, couchdb address etc.) are defined in `DB_Constants.py` 
## Prerequisites
### Python packages
* Tweepy
* Couchdb
* json
* time
* Shapely
* re
## Running
Testing Twitter Havester on localhost:
- Run the Searcher
```
python3 Searcher.py
```
- Run the Streamer
```
python3 Streamer.py
```
