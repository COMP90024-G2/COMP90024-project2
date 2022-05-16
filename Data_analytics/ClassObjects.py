#Define Class Objects

class Tweet:

    def __init__(self, tweet_info):
        self.coords = tweet_info['doc']['geo']['coordinates']
        self.text = tweet_info['doc']['text']
        self.language = tweet_info['doc']['lang']

class District:

    def __init__(self, raw_geo_info):
        self.sa3name = raw_geo_info['properties']['sa3_name16']
        self.sa3code = raw_geo_info['properties']['sa3_code16']
        self.shape = raw_geo_info['geometry']['type']
        self.coords = raw_geo_info['geometry']['coordinates']
        self.tweet_list = []
        self.tweet_count = 0
        self.languages = {}
        self.mean_emotion_score = 0
        self.positive_tweet_percentage = 0
        self.negative_tweet_percentage = 0
        self.neutral_tweet_percentage = 0
        self.mean_employment_opinion_score = 0
        self.mean_healthcare_opinion_score = 0
        self.aurin_lang= {}
        self.aurin_income = {}
        self.aurin_health = {}

    def add_tweet(self, tweet):
        self.tweet_count += 1
        self.tweet_list.append(tweet)

    def count_languages(self, tweet_list):
        for tweet in tweet_list:
            if tweet.language in self.languages.keys():
                self.languages[tweet.language] += 1
            else:
                self.languages[tweet.language] = 1
                 

class City:

    def __init__(self):
        self.districts = {}
        
    def add_district(self, district):
        self.districts[str(district.sa3code)] = district

