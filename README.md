# Yelp Project
Yelp Project at  Flatiron School Phase 1 

Overview:
======
When starting a business, the most important factor to consider is to whether to start your business in one location or another. At Prometheus Adventures we deal with helping our customers decide where to setup their businesses, by using sophisticated API's to give the most detailed report on where to set up the a business.

# Target: 
For this analysis, we are analyzing where to setup a Yoga businesses within NYC and London using Yelp's API.

<p align="center">
 <img width="360" height="120" src=images/Yelp.png>
 </p>

Yelp utlizes many various attributes when looking for a certain types of business. Whether it is output of a business location, the type of business, how expensive that business is, or the amount of reviews that business has. By utilizing Yelp's API called fusion, we are able to provide to our customer what is the best location that business should be set up in. By taking in various condtions based on the Yelp API we can provide a detail report based on the factors that decide the succes of a business.

# Repository
All data sets can be found in the Yelp.db files, functions we use to sift through the data can be found in the functions file, and all images and graphs can be found in the image folder. 

# Analysis Focus
1. All analysis focues on the data given by Yelps Fusion API that in constantly updated on a regular basis.
2. The analysis focus on business with the most review counts, hgihest average ratings, and reveiws given. 

# Analysis 
Our first analysis was determing the pricing with the number of observations we have for each city. One discrepancy that we found in Yelp's API database for pricing was that not all the businesses had pricing info. This created a smaller dataset for each location. Our analysis in determing the pricing for the number of business is sufficent for determing where to put our business based on pricing information. The infograph displays the count of the least expensive yoga studios in comparison to the most expensive yoga studios based on location. Least expensive yoga studios being shown on the graph by the numeric number value 1; the most expensive yoga studios being shown by the numeric value 4. Based on on the prefence of our customers, see that London, has a higher cost for the yoga studios that customers are willing to pay for in comparison to NYC where yoga studios are more reasonably priced. We have the same number population but what people are paid in salaries based on current inflation is much greater in London in comparison to NYC.

<p align="center">
  <img width="500" height="450" src=images/Pricing_Yoga_Location.png>
</p>

# Averages of Ratings and Review Counts

We fist wanted to see the average rating for each location based on which country the potential business would be located in. Soley based on the average rating, we have concluded that NYC is a more sutiable location for opening a yoga studio. There are more higher ratings in the city of NYC denoted as US, in comparison to London denoted as GB. One discrepancy is that in London, yelp is not a source that is used that often by businesses for local searches by customers. 

<p align="center">
  <img width="500" height="450" src=images/Average_Rating_Location.png>
</p>

We have seen how the distrubtion on pricing can make or break business depending on what type of clientele they cater to, now we want to take this one step further to see what is average reviews for each location. This insight will help us determing which location values Yoga a source for exercise. We see that NYC receives far higher averages and range of reviews per yoga studio then that of London. One reason for this descrepency as we mention above, is that London businesses does not use the Yelp app to store their busineaa information for customers to discover them. Even with this discrepency, our data tells us that NYC yoga studios are by far more valued than in comparison to London. 



<p align="center">
  <img width="650" height="450" src="images/Average_Reviews_locations.png">
</p>



# Reviews By Zip Code

Our final analysis honed down specifically on Brooklyn and Central London. In both of these locations we see an influx of residents residing and the wealth per capita has increased significantly in these areas. From this idea, we realized that people with more money have more time and resources to allocated to their health. Yoga now being one of the most popular trends when it comes to health of the body and mind. We see that on average in Central London the number of reviews being made are just around 1 for each zip code. With Brooklyn we are seeing roughly 12 reviews for each zip code showing how the people of Brooklyn value the practice of yoga much more than in Central London. 


<p align="center">
  <img width="650" height="450" src="image/Reviews_in_London_of_Yoga_Studios copy.png">
</p>

<p align="center">
  <img width="650" height="450" src="images/Reviews_in_Brooklyn_of_Yoga_Studios.png">
</p>



# Summary
From the analysis done at Prometheus Adventures considering multiple conditions based on these two cities we have concluded that opening a yoga studio is best in Brooklyn, NY. We have decided the is the best decision for our client based on anaylsis seen above. We see that Brooklyn has more reviews, the cost of for running a yoga studio is moderalty cheaper based on the prices their customers will have to pay, and that the customers in Brooklyn. Another crucial factor is how NYC values their health more when it comes to having Yoga to facilite their health needs. Leading to the conclusion that Brooklyn is the best location to open a brand new yoga studio. 


# Presentation 

[Presentation](https://github.com/Astroraf/Yelp_Project/blob/main/Yelp%20Project%20Presentation%20.pdf)



# Contributors 

[Rafael Ferreira](https://github.com/Astroraf)

[John Silverman](https://github.com/silvermanjonathan) 
