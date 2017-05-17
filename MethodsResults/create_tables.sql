CREATE TABLE closed_restaurants
   (num integer,
   name varchar(50),
   business_id varchar(50),
   review_count integer,
   is_open integer,
   stars integer,
   city varchar(50),
   categories varchar(50));

.separator ","
.import Closed_restaurants.csv closed_restaurants

CREATE TABLE open_restaurants
   (num integer,
   name varchar(50),
   business_id varchar(50),
   review_count integer,
   is_open integer,
   stars integer,
   city varchar(50),
   categories varchar(50));

.separator ","
.import Open_restaurants.csv open_restaurants

CREATE TABLE reviews
   (num integer,
   	reviews varchar(50),
   	dates varchar(50),
   	stars integer,
   business_id varchar(50));

.separator ","
.import reviews.csv reviews

CREATE TABLE yelp_reviews
   (num integer,
      texts varchar(50),
      dates varchar(50),
      stars integer,
   business_id varchar(50));

.separator ","
.import yelp_reviews.csv yelp_reviews