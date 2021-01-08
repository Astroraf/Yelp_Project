
import json
import requests
import numpy as np

#Connection to the Yelp API with the keys created 
client_id = "WdeBQ0QfW7ctlNNGDyNEwA"
api_key = "qOP1w_dBiefuyHCkz5gzIlhtKzNxBNMi3uCVJib_Kzs_y0EKqn1pKpRlpGvAPmB2fZ_eVWv65j_o5rmiT9HNK10tH5rosM3GfauVdQU0TvfOtdqn4L3zzLC2g1P3X3Yx"

#Creates a header with the attached API key from the Yelp API
headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

def yelp_call(url, url_params, api_key):
    # your code to make the yelp call
    response = requests.get(url, headers=headers, params=url_params)
    data = response.json()
    return data
    
    
# Creating a function that parses that data then returns the information as a tuple
def parse_results(results):
#empty list of all the information we want to pull for the yoga businesses 
    biz_list = []

    #Iterate through all the businesses keys to pull out the relvant information from each key
    for business in results['businesses']:
        for item in ['businessID', 'rating', 'price', 'name', 'review_count', 'city', 'country', 'zip_code']:
            #If the value is not found for a given key then replace it with a NAN value
            if item not in business:
                business[item] = np.nan
            else: 
                business[item]
        #Grabs each value and appends to a list
        biz_tuple = ( business['id'], 
                      business['rating'],
                      business['price'],
                      business['name'],
                      business['review_count'],
                      business['location']['city'],
                      business['location']['country'],
                      business['location']['zip_code']
                      )    
        biz_list.append(biz_tuple)
    return biz_list
    
#Takes the values from the parsed results and inputs them into the business table
def insert_values(conn, cur, parse_results):
        add_business = ("""
    INSERT INTO businesses (businessID, rating, price, name, review_count, city, country, zip_code)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?) """)
        cur.executemany(add_business, parse_results)
        conn.commit()
        

#Grabs all three reviews for each business when we input the ID from the business list 
#Created above and then outputs a dataframe 

def yelp_call_reviews(ID):
        url = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(ID)
    # your code to make the yelp call
        response = requests.get(url, headers=headers)
        data = response.json()
        
#We need to know parse the inforamtion given from the reviews table 
def parse_reviews(businessID, review_results):
    #Creates a tuple list of all the information extract from the Yelp reveiws for each 
    #business 
    tuple_lists = []
    
    #Checks if there is a missing reveiw and returns None if there is a missing review
    if 'error' in review_results:
        if review_results['error']['code'] == 'BUSINESS_UNAVAILABLE':
            return None
     #else check for missing values for the within the keys and returns none       
    else:
        for review in review_results['reviews']:
            for item in ['text', 'rating', 'time_created']:
                if item not in review:
                    review[item] = np.nan
                #Populates the a tuple list if the value is present
                review_tuple =( businessID, 
                                review['text'],
                                review['rating'],
                                review['time_created'],
                                review['id']
                              )
                tuple_lists.append(review_tuple)
    
    return tuple_lists
        return data
        
def insert_reviews(conn, cur, parse_reviews):
        add_reviews = ("""
        INSERT INTO reviews (businessID, text, rating, time_created, reviewID)
        VALUES (?, ?, ?, ?, ?) """)
        cur.executemany(add_reviews, parse_reviews)
        conn.commit()
