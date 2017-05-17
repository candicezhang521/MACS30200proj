import pandas as pd

LV_restaurants_df = pd.read_csv('LV_restaurants.csv',header=0)

is_closed_count = len(LV_restaurants_df[LV_restaurants_df['is_open'] == 0])
#is_closed_restaurants = LV_restaurants_df[LV_restaurants_df['is_open'] == 0]
#is_closed_restaurants = is_closed_restaurants.drop(is_closed_restaurants.columns[[0]], axis=1) 
#is_closed_restaurants.to_csv('Closed_restaurants.csv', sep = ',', encoding = 'utf-8')

is_open_count = len(LV_restaurants_df[LV_restaurants_df['is_open'] == 1])
#is_open_restaurants = LV_restaurants_df[LV_restaurants_df['is_open'] == 1]
#is_open_restaurants = is_open_restaurants.drop(is_open_restaurants.columns[[0]], axis=1) 
#is_open_restaurants.to_csv('Open_restaurants.csv', sep = ',', encoding = 'utf-8')
print('There are',is_closed_count,'restaurants that are closed')
print('There are',is_open_count ,'restaurants that are still open.')
