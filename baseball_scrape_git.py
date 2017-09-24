from urllib import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
from time import sleep
import sys
reload(sys)†
sys.setdefaultencoding('utf-8')

def scrape(url, name):
""" Takes baseball player URL and name, pulls player batting or pitching statistics
    and saves it to a mongoDB database. """

    
# establish a connection to Mongodb database and collection
    connection = MongoClient()
    db = connection['capstone']
    collection = db['baseball']

# create BeautifulSoup object of the player url
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

# player_data_rows collects rows of baseball statistics for each player
    player_data_rows = soup.findAll('tr')[1:]

# some players have empty URL pages, if the page is empty no data will be pulled
# and the code will move on to the next player
    if len(player_data_rows) == 0:
        print "No tables in website", name, len(data_rows)
        return None

    player_index_list = []
    sleep(2)
    for index,data_row in enumerate(player_data_rows):
        if data_row.find('th').getText() == 'Year' or len(data_row.find('th').getText()) > 7:
            player_index_list.append(index)

# try and except statement insures the correct player data rows are selected
    try:
        player_data_rows = soup.findAll('tr')[1:player_index_list[0]+1]
    except:
        player_data_rows = soup.findAll('tr')[1:]


# for loop creates a list of columns headers
    stat_headers = ['Player']
    for i in soup.findAll('tr')[1].findAll('th'):
        stat_headers.append(i['data-stat'])
    for i in soup.findAll('tr')[1].findAll('td'):
        stat_headers.append(i['data-stat'])

# for loop adds player statistics to the player data list
    for i in range(len(player_data_rows)):
        player_data = [name]
        for th in data_rows[i].findAll('th'):
            player_data.append(th.getText())
        for td in data_rows[i].findAll('td'):
            player_data.append(td.getText())

# once the stat_headers and player_data lists are established we import them
# into our mongoDB collection
        collection.insert_one(dict(zip(stat_headers, player_data)))
