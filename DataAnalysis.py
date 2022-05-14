# General Data analysis functions

from UtilityFunctions import *
from ClassObjects import *
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer

def count_languages(melb_city):
    for district in melb_city.districts:
        melb_city.districts[district].count_languages(melb_city.districts[district].tweet_list)


def general_sentiment_analysis(melb_city):
    for district in melb_city.districts:

        txt_lst = generate_english_text_list(melb_city.districts[district])

        positive_tweet_count = 0
        negative_tweet_count = 0
        neutral_tweet_count = 0

        sum_score = 0

        for txt in txt_lst:
            score = TextBlob(txt).sentiment.polarity
            sum_score += score
            if score > 0:
                positive_tweet_count += 1
            elif score < 0:
                negative_tweet_count += 1
            elif score == 0:
                neutral_tweet_count += 1

        if len(txt_lst) != 0:
            melb_city.districts[district].mean_emotion_score = sum_score/len(txt_lst)
            melb_city.districts[district].positive_tweet_percentage = positive_tweet_count/len(txt_lst)
            melb_city.districts[district].negative_tweet_percentage = negative_tweet_count/len(txt_lst)
            melb_city.districts[district].neutral_tweet_percentage = neutral_tweet_count/len(txt_lst)
        else:
            melb_city.districts[district].mean_emotion_score = 0

def topic_sentiment(topic_text_list):
    sum_score = 0

    if len(topic_text_list) != 0:
        for txt in topic_text_list:
            sum_score += TextBlob(txt).sentiment.polarity

        return  sum_score/len(topic_text_list)


def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    lemmatized=[]
    for word in text:
        lemmatized.append(lemmatizer.lemmatize(word))
    return lemmatized

def simple_tweet_categorization(text_list, topic1, topic1_words, topic2, topic2words):
    topic1_txt = []
    topic2_txt = []
    for txt in text_list:
        temp = lemmatize_text(txt)
        for word in topic1_words:
            if word in temp:
                if txt not in topic1_txt:
                    topic1_txt.append(txt)
        for word in topic2words:
            if word in temp:
                if txt not in topic2_txt:
                    topic2_txt.append(txt)
    return {topic1: topic1_txt, topic2: topic2_txt}

def topic_sentiment_analysis(melb_city, employment_keywords, health_keywords):
    employment_keywords = employment_keywords + load_txt("business.txt")
    for district in melb_city.districts:
        text_list = generate_english_text_list(melb_city.districts[district])
        categorized_tweet = simple_tweet_categorization(text_list, "Employment", employment_keywords, "Health", health_keywords)
        melb_city.districts[district].mean_employment_opinion_score = topic_sentiment(categorized_tweet["Employment"])
        melb_city.districts[district].mean_healthcare_opinion_score = topic_sentiment(categorized_tweet["Employment"])    
        
