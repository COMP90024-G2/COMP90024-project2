# Utility Functions

import json
import re
import string
from ClassObjects import City,District
from AurinData import *

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
    try:
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
    except Exception:
        return

def load_txt(file_name):
    list_word=[]
    try:
        with open(file_name) as phrases:
            for word in phrases:
                word = word.lower()
                word = re.sub(r'[^\w\s]','',word)
                word = word.strip()
                word = word.split()
                i=0
                temp_word=''
                while i < len(word):
                    temp_word = temp_word+" "+word[i]
                    temp_word = temp_word.lstrip()
                    i+=1
                list_word.append(temp_word)
    except Exception as e:
        print(e)
    return list_word


def generate_english_text_list(district):
    txt_lst = []
    for tweet in district.tweet_list:
        if tweet.language == 'en':
            txt_lst.append(txt_preprocess(tweet.text))
    return txt_lst  

def remove_punctuations(text):
    text = text.translate(str.maketrans('', '',string.punctuation))
    return text

def txt_preprocess(text):
	text = re.sub(r'https?:\/\/\S*', '', text, flags=re.MULTILINE)
	return remove_punctuations(text)

def synonym_extractor(phrase):
    synonyms = []
    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            if l.name() not in synonyms:
                try:
                    synonyms.append(l.name().replace('_',' '))
                except Exception:
                    continue
    return synonyms

def antonym_extractor(phrase):
    antonym = []
    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            if l.name() not in antonym:
                try:
                    antonym.append(l.antonyms()[0].name().replace('_',' '))
                except Exception:
                    continue
    return antonym

def generate_keywords(root_words):
    keyword_list = []
    for word in root_words:
        synonyms = synonym_extractor(word)
        antonyms = antonym_extractor(word)
        for syn in synonyms:
            if syn not in keyword_list:
                keyword_list.append(syn)
        for ant in antonyms:
            if ant not in keyword_list:
                keyword_list.append(syn)
    return keyword_list


def condense_output(melb_city):

    output = {"features":[]}
    for district in melb_city.districts:
        temp = {}
        temp = {"type":"Feature","geometry":{}, "properties" : {}}
        temp["properties"]["sa3name"] = melb_city.districts[district].sa3name
        temp["properties"]["sa3code"] = melb_city.districts[district].sa3code
        temp["geometry"]["type"] = melb_city.districts[district].shape
        temp["geometry"]["coordinates"] = melb_city.districts[district].coords
        temp["properties"]["tweet_count"] = melb_city.districts[district].tweet_count

        temp["properties"]["general_emotion"] = melb_city.districts[district].mean_emotion_score
        temp["properties"]["positive_tweets_percent"] = melb_city.districts[district].positive_tweet_percentage
        temp["properties"]["neutral_tweets_percent"] = melb_city.districts[district].neutral_tweet_percentage
        temp["properties"]["negative_tweets_percent"] = melb_city.districts[district].negative_tweet_percentage
        temp["properties"]["employment_attitude"] = melb_city.districts[district].mean_employment_opinion_score
        temp["properties"]["healthcare_attitude"] = melb_city.districts[district].mean_healthcare_opinion_score

        temp["properties"]["aurin_language"] = melb_city.districts[district].aurin_lang
        temp["properties"]["aurin_income"] = melb_city.districts[district].aurin_income
        temp["properties"]["aurin_health"] = melb_city.districts[district].aurin_health

        en_count = 0
        total = 0
        for language in melb_city.districts[district].languages:
            total += melb_city.districts[district].languages[language]
            if language == "en":
                en_count = melb_city.districts[district].languages[language]
                
        try:
            temp["properties"]["proportion_non_english_tweets"] = 1 - en_count/total
        except Exception:
            temp["properties"]["proportion_non_english_tweets"] = 0
            output["features"].append(temp)
            continue

        output["features"].append(temp)

    return output