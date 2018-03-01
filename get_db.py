import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from get_info import GetInfo

movie_name = 'Red Sparrow'
Red = GetInfo(movie_name, 'https://www.rottentomatoes.com/m/red_sparrow/reviews/')

columns = ['Movie', 'Critic', 'Score', 'Yield']
data = pd.read_csv('~/Documents/rt_critics_project/db.csv', names=columns)

movie_list = []
score_list = []
for n in range(len(Red.names_list())):
    movie_list.append(movie_name)
    score_list.append(Red.score())

data['Movie'] = movie_list
data['Critic'] = Red.names_list()
data['Score'] = score_list
data['Yield'] = Red.yeld()

print(data)
