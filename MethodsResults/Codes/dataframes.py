import pandas as pd 
import numpy as np 
business_df = pd.read_csv('yelp_academic_dataset_business.csv',header=0)
del business_df['address']
del business_df['hours']
del business_df['type']
del business_df['neighborhood']
del business_df['state']
del business_df['postal_code']
del business_df['latitude']
del business_df['longitude']
del business_df['attributes']
business_df['name'] = business_df.name.str.replace('(b[\'\"]?)*([\'\"])' , '')
business_df['business_id'] = business_df.business_id.str.replace('(b[\'\"]?)*([\'\"])' , '')
business_df['city'] = business_df.city.str.replace('(b[\'\"]?)*([\'\"])' , '')

business_df.to_csv('businesses.csv', sep = ',', encoding = 'utf-8')
