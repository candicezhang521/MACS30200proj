import pandas as pd 
import numpy as np 
reviews_df = pd.read_csv('yelp_academic_dataset_review.csv',header=0)
del reviews_df['type']
del reviews_df['funny']
del reviews_df['cool']
del reviews_df['useful']
del reviews_df['user_id']
del reviews_df['review_id']
reviews_df['text'] = reviews_df.text.str.replace('(b[\'\"]?)*([\'\"])' , '')
reviews_df['business_id'] = reviews_df.business_id.str.replace('(b[\'\"]?)*([\'\"])' , '')
reviews_df['date'] = reviews_df.date.str.replace('(b[\'\"]?)*([\'\"])' , '')

reviews_df.to_csv('yelp_reviews.csv', sep = ',', encoding = 'utf-8')
