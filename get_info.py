import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


class GetInfo:
    #change the raw_page variable to the movie link and add the name of the movie
    def __init__(self, name, page):
        self.page = page
        self.name = name
        self.link = requests.get(self.page)
        self.soup = BeautifulSoup(self.link.content, 'html.parser')

    #list of reviews
    def review_list(self):
        raw_rev = self.soup.find_all(class_='the_review')
        reviews = []
        for rev in range(len(raw_rev)):
            reviews.append(raw_rev[rev].get_text())
        return reviews



    #list of links for full reviews
    def link_list(self):
        links = []
        for link in self.soup.find_all('a', attrs={'href': re.compile("^https://")}, text='Full Review'):
            links.append(link.get('href'))
        return links

    #list of critics names & magazines
    def names_list(self):
        raw_names = self.soup.find_all(class_='col-sm-13 col-xs-24 col-sm-pull-4 critic_name')
        names = []
        for n in range(len(raw_names)):
            nm = raw_names[n].get_text()
            name, mag = nm.strip().split('   ')
            names.append(name)
        return names

    #tomatometer Score
    def score(self):
        score = self.soup.find('span', class_='tMeterScore').get_text()
        return score

    #fresh/rotten label for the reviews
    def yeld(self):
        yeld_list = []
        raw_yeld = self.soup.find_all(class_='col-xs-16 review_container')
        for n in range(len(raw_yeld)):
            if 'fresh' in str(raw_yeld[n]):
                yeld_list.append('Fresh')
            elif 'rotten' in str(raw_yeld[n]):
                yeld_list.append('Rotten')
        return yeld_list

Red = GetInfo('movie_name', 'https://www.rottentomatoes.com/m/red_sparrow/reviews/')
