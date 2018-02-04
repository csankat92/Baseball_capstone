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

Ultimately I decided to classify a major leaguer based on if a player has played 3 seasons in the majors or if they were in the minor leagues in 2015 and have 2 years of major league experience. My logic is often times major leaguers get injured and that can force a minor leaguer into the majors, thus 1 or 2 seasons shouldn't warrant a success. 3 seasons indicates the player has showcased major league talent and proven he belongs in the major leagues. Now some players simply aren't old enough to have played 3 seasons in the majors, but have major league talent and have the minor league statistics to back that up. In an attempt to include these players I created the criteria if a player plays in the minors in 2015 and has 2 seasons in the majors than he is a success. 

More Data Organizing
---
Having classified successful players I needed to re-organize my data for exploration and eventually for training on a machine learning algorithm. 

Taking the data in the image above I had to condense the data into single rows for each player and include only minor league statistics. To condense the data I did a series of group-by clauses with aggregations to narrow the player data into single rows. 

Performing these group-by clauses gets my data into a format where I can begin my exploration and pinpoint those key features that actually determine what makes a major leaguer. 

<img width="880" alt="screen shot 2018-02-03 at 5 46 27 pm" src="https://user-images.githubusercontent.com/28715286/35772811-34dc2b8a-090a-11e8-8580-6e48025d50b4.png">


Data Mining
---

I begin my exploration by creating graphs that compare the Major League Graduation Percentage v.s features within my data. My first stop on this journey is Age Difference. 

This feature describes how old a player is versus his competition. Ex. If a player is 20 and is playing in a specific minor league where the average age is 22, his age difference will be -2. 

The graph below shows as Age Difference increases the chance of making it to the majors decreases. In fact if you have an age difference greater than 0 your chances of making it to the majors drops to 3% and less. 

<img width="883" alt="screen shot 2018-02-03 at 6 27 55 pm" src="https://user-images.githubusercontent.com/28715286/35773172-01684c88-0910-11e8-9f9f-081228786cad.png">

Next up Slugging Percentage: 

Slugging best describes a player proficency as a batter. In the graph below we see as slugging increases the chances of making to the majors also increase. The idea is if you are consistenly performing at the plate and hitting homeruns, triples and doubles you most certainly are going to hit the majors. 

<img width="847" alt="screen shot 2018-02-03 at 6 41 05 pm" src="https://user-images.githubusercontent.com/28715286/35773242-d197cf04-0911-11e8-88dd-913fc108646d.png">

Lastly we have AZFL1 or Arizona Fall League:

This feature is simply a dummy variable for if a minor league player played in the Arizona Fall League. The Arizona Fall League is a post minor season league where the most well regarded prospects will be sent to to play against the best competition in the minor leagues. As we seen in the graph if you attend the the Arizona Fall League your chances of graduating to the majors increases by 53%. 

<img width="815" alt="screen shot 2018-02-03 at 7 15 23 pm" src="https://user-images.githubusercontent.com/28715286/35773399-a61eecea-0916-11e8-91ad-892606a9307b.png">

Model Building
---

Having explored my dataset and an idea on which features will influence my model it's time to build.

I am choosing to only include Age, Age_difference, Slugging, Batting Avg., Runs Batted In per At Bat and Number of Minor League Seasons as the features for the model. I am also splitting my dataset into a train and test sample. I will test my trained model against the test sample to determine the accuracy of the model. 

<img width="777" alt="screen shot 2018-02-03 at 7 33 44 pm" src="https://user-images.githubusercontent.com/28715286/35773468-3da8abbc-0919-11e8-84f5-74d4729e9cb9.png">

<img width="744" alt="screen shot 2018-02-03 at 7 33 51 pm" src="https://user-images.githubusercontent.com/28715286/35773465-34115b44-0919-11e8-86d8-1188f4da60a7.png">


After training my model it produced the following results. 

<img width="433" alt="screen shot 2018-02-03 at 7 50 18 pm" src="https://user-images.githubusercontent.com/28715286/35773564-868b0c74-091b-11e8-832c-6a83f300cf18.png">

I am not focused on accuracy because knowing only 9% of minor leagues graduate to the majors if I told my model to say no everytime it needed to make a prediction it would be correct 91% of the time. Instead, I want to measure the success of model based on recall and precision. Recall states my models ability to detect the minor leagues that have graduated to the majors. Precision states given that my model has predicted this prospect will make it to the majors what are the chances I am correct. 

On my first testing of the model it does a fair job based on Recall and Precision, but my goal isn't to create a model that would get a C+ on a history test.

Following some brainstorming I noticied my model is failing to pick up on the characteristics of a success with so few minor leagurs graduating to the majors. I then decide downsample the majority class using the resample function. 

<img width="873" alt="screen shot 2018-02-03 at 8 14 23 pm" src="https://user-images.githubusercontent.com/28715286/35773695-dc83b074-091e-11e8-9c1b-78da04d1b1ff.png">

I then re-train my model and get the following results. 

<img width="424" alt="screen shot 2018-02-03 at 8 15 13 pm" src="https://user-images.githubusercontent.com/28715286/35773700-fc3f3f78-091e-11e8-9926-e7d38bc7a635.png">

Downsampling signficantly improves my model Recall and Precision metrics. 

Real World Test Case
---
In 2004, Alex Rodriguez was traded from the Texas Rangers to the New York Yankees. 

![Alt Text](https://media.giphy.com/media/3ohs4wqbOH0TANtHAQ/giphy.gif){:height="50%" width="50%"}









 

