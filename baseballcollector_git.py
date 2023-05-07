from urllib import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from baseball_scrape import scrape
import re
import timeit


html = urlopen('https://www.baseball-reference.com/register/player.fcgi')
# created BeautifulSoup object that collects player URL's organized by last name
# and stores them in the url_list

soup = BeautifulSoup(html, 'lxml')
lastname_list = []
for i in soup.findAll('a'):
    lastname_list.append(i['href'])

url_list = filter(lambda x: len(x) == 31, lastname_list)

# for loop iterates through each item in URL list and for each item
# a BeautifulSoup object is created
for i in url_list[1:379]:
    html = urlopen('https://www.baseball-reference.com' + i)
    soup1 = BeautifulSoup(html, 'lxml')

# href_list contains all URLs in the BeautifulSoup object
    href_list = [i['href'] for i in soup1.findAll('a')]
# name list contains all the players names in the BeautifulSoup object
    name_list = [i for i in soup1.findAll('div', 'section_content')]
    player_url_list = []

# for loop iterates through the href_list and the regular expression selects
# player URLs and adds them to the player_url_list

# at the completion of the loop the player_url_list and name_list will be the
# same length
    for url in href_list:
        r = re.search('(/register/player.cgi.*)',url)
        if r:
            player_url_list.append(r.group(0))

#  enumerate function allows the for loop to iterates through names and create an
# index for each name. We will used the index to to find the desired player URL.
 
# scrape_input includes the player url and name which is needed to run the
# baseball webscraper called scrape
    for index, names in enumerate(name_list[0].findAll('a')):
        scrape_input = ['https://www.baseball-reference.com' + player_url_list[index] ,names.getText().encode('ascii', 'ignore')]
        scrape(scrape_input[0], scrape_input[1])
        sleep(2)
