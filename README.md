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

Identifying a Success
---
Before I can move on I had to classify what makes a major leaguer. Is it one season in the majors? How about 2 seasons? Maybe a major leaguer is a player who hits over 50 homeruns in his career? 

Ultimately I decided to classify a major leaguer based on if a player has played 3 seasons in the majors or if they were in the minor leagues in 2015 and have 2 years of major league experience. My logic said often times major leaguers get injured and that can force a minor leaguer into the majors, thus 1 or 2 seasons shouldn't warrant a success. 3 seasons indicates the player has showcased major league talent and proven he belongs in the major leagues. Now some players simply aren't old enough to have played 3 seasons in the majors, but have major league talent and have the minor league statistics to back that up. In an attempt to inlcude these players I created the criteria if player plays in the minors in 2015 and has 2 seasons in teh majors than he is a success. 

More Data Organizing
---

My data organization is not done. From here I had to condense the data into a single row for each player and include only minor league statistics. To condense the data I did a series of group-by clauses to narrow the player data into single rows. 

Now my data looks like this.

![App Architecture](https://github.com/csankat92/Baseball_capstone/blob/master/images/Screen%20Shot%202017-10-23%20at%209.42.22%20AM.png)







  
 

