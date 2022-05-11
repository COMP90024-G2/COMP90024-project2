# Utility Functions

import json
import re
from ClassObjects import City,District,Tweet
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import nltk
#nltk.download('omw-1.4')
from nltk.corpus import wordnet

def initialize_melb_area(geofile):
    melb = City() 
    with open(geofile,'r') as f:
        geoinfo = json.load(f)
        for i in range(len(geoinfo['features'])):
            melb.add_district(District(geoinfo['features'][i]))
    return melb

def locate_tweet_to_Area(tweet, melb):
    tweet_coor = tweet.coords
    loc = Point([tweet_coor[1],tweet_coor[0]])
    for district in melb.districts:
        if melb.districts[district].shape == 'Polygon':
            container_box = Polygon(melb.districts[district].coords[0])
            if container_box.contains(loc):
                melb.districts[district].add_tweet(tweet)
        elif melb.districts[district].shape == 'MultiPolygon':
            for polygon in melb.districts[district].coords:
                container_box = Polygon(polygon[0])
                if container_box.contains(loc):
                    melb.districts[district].add_tweet(tweet)
    return False

def generate_english_text_list(district):
    txt_lst = []
    for tweet in district.tweet_list:
        if tweet.language == 'en':
            txt_lst.append(txt_preprocess(tweet.text))
    return txt_lst  

def txt_preprocess(text):
	text = re.sub(r'https?:\/\/\S*', '', text, flags=re.MULTILINE)
	return text.replace('@',' ').replace('/',' ').replace(':',' ').replace('#',' ').replace(',',' ').replace("\\",' ').replace('.',' ').replace('!',' ').replace('?',' ').lower()

def synonym_extractor(phrase):

    synonyms = []

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            if l.name() not in synonyms:
                synonyms.append(l.name().replace('_',' '))

    return synonyms

def generate_keywords(root_words):
    keyword_list = []
    for word in root_words:
        synonyms = synonym_extractor(word)
        for syn in synonyms:
            if syn not in keyword_list:
                keyword_list.append(syn)
    return keyword_list

def simple_tweet_categorization(text_list, topic1, topic1_words, topic2, topic2words):
    topic1_txt = []
    topic2_txt = []
    for txt in text_list:
        for word in topic1_words:
            if word in txt:
                if txt not in topic1_txt:
                    topic1_txt.append(txt)
        for word in topic2words:
            if word in txt:
                if txt not in topic2_txt:
                    topic2_txt.append(txt)
    return {topic1: topic1_txt, topic2: topic2_txt}

def output_to_json(melb_city):
    output = {}
    for district in melb_city.districts:
        
        output[district] = {}
        output[district]["sa3name"] = melb_city.districts[district].sa3name
        output[district]["sa3code"] = melb_city.districts[district].sa3code
        output[district]["shape"] = melb_city.districts[district].shape
        output[district]["coordinates"] = melb_city.districts[district].coords
        output[district]["tweet_count"] = melb_city.districts[district].tweet_count

        output[district]["language"] = {}
        for language in melb_city.districts[district].languages:
            output[district]["language"][language] = melb_city.districts[district].languages[language]

        output[district]["general_emotion"] = melb_city.districts[district].mean_emotion_score
        output[district]["positive_tweets_percent"] = melb_city.districts[district].positive_tweet_percentage
        output[district]["neutral_tweets_percent"] = melb_city.districts[district].neutral_tweet_percentage
        output[district]["negative_tweets_percent"] = melb_city.districts[district].negative_tweet_percentage
        output[district]["employment_attitude"] = melb_city.districts[district].mean_employment_opinion_score
        output[district]["healthcare_attitude"] = melb_city.districts[district].mean_healthcare_opinion_score
        
        # load aurin data

    return json.dumps(output, indent = 4)