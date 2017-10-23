# Baseball_capstone

Overview
---
Every year as the MLB trade deadline approaches losing teams exchange veterans with winning teams for prospects. The hope is that those prospects will turn around to become great major league baseball players. 

As much as major league teams would like minor leaguers to easily transition to the majors the process isn't easy and only 10% of prospects actually graduate to the major league. My goal is aid in the player selection process and build a model that takes minor league baseball statistics and predict whether or not a minor leaguer will actually "make it".

Data Sources
---
* Baseball-Reference.com via web-scraper (baseball_scrape & baseball_collector python scripts) 

Technology 
---
* Python 
  - BeatifulSoup for web scraping 
  - Pandas and Numpy for data processing
  - Matplotlib and Seaborn for data visulizations
  - SciKit Learn Logistic Regression and Random Forest Classifier
* MongoDB
  - Once data was scraped it was stored in a Mongo Database
* Amazon Web Services
  - Ran python web-scraper on multiple EC2 instances 
  
Data Cleaning & Organizing
---
Having gathered all necessary minor and major league statistics I removed all players without a minor league history prior to the year 2000. I established the cut off because of a number of rule changes in the minors and major leagues. Amongst the players in my data I also had over a thousand non-MLB affilated players such as players in foreign or independent leagues, these players were removed as they were not pertenant to solving my problem. 

At this point in time I was working with data that looked like the image below. 

![App Architecture](https://github.com/csankat92/Baseball_capstone/blob/master/images/Screen%20Shot%202017-10-23%20at%209.13.54%20AM.png)



  
 

