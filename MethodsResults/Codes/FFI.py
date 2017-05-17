import nltk
import sqlite3
import re
import json
import pandas as pd
from nltk import *
from nltk.tag import *
from nltk.corpus import stopwords
from nltk.sentiment import *
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment.util import *



def find_business_id(is_open):
    '''
    The end results is to return a unique list of strings
    '''
    yelp_db = sqlite3.connect('yelp.db')
    c = yelp_db.cursor()

    if is_open:
        query = 'SELECT DISTINCT business_id FROM open_restaurants;'
    else:
        query = 'SELECT DISTINCT business_id FROM closed_restaurants;'

    r = c.execute(query)
    results = r.fetchall()
    business_id_lst = []
    #print(results)
    for i in range(len(results)):
        business_id_lst.append(results[i][0])

    return business_id_lst[1:]

def find_reviews_by_year(business_id):
    '''
    The end results is to return a list of strings
    '''
    yelp_db = sqlite3.connect('yelp.db')
    c = yelp_db.cursor()
    query = 'SELECT reviews,dates FROM reviews WHERE business_id = ?;'
    #query_date = 'SELECT dates FROM reviews WHERE business_id = ?;'
    r = c.execute(query, [business_id])
    results = r.fetchall()
    #print(results)
    review_by_year_dict = {}
    reviews_lst = []
    for i in range(len(results)):

        text = results[i][0]
        dates = results[i][1]
        #print('hh',text)
        #print(type(dates))
        year = re.findall('((\d){4})',dates)[0][0]
        #print(year)
        if year not in review_by_year_dict:
            review_by_year_dict[year] = []

        review_by_year_dict[year].append(text)
    return review_by_year_dict


# business_id_lst = find_business_id(is_open=False)
# test_business_id = 'BvV9SSaQhC4fvpC3XyQjjA'
# test_review = find_reviews_by_year(test_business_id)
# print(test_review)


