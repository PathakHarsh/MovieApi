
from selenium import webdriver
from bs4 import BeautifulSoup, dammit
import pandas as pd
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieDetails.settings')

import django
django.setup()
from Details.models import Movie
print("test")

browser = webdriver.Chrome()

browser.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")


content = browser.page_source
soup = BeautifulSoup(content)
# print("soup",soup)    

table = soup.find('table',attrs={'data-caller-name':'chart-top250movie'})


body = table.find("tbody")
# print(body.findAll("tr")) 
# print(table)
# movie_driver = webdriver.Chrome()
movie_driver = webdriver.Chrome()

all_trs = body.findAll("tr")
all_trs = all_trs[78:]
for a in all_trs:

    try:
        name_td = a.find('td',attrs={'class':"titleColumn"})
        anchor = name_td.find("a")
        movie_title = anchor.text
        print(movie_title)
        # print(anchor)
        
        #rating
        rating_td = a.find('td',attrs={'class':"imdbRating"})
        # print("-----",rating_td)
        strong_box = rating_td.find("strong")
        rating = strong_box.text
        print("rating",rating) 



        print("link",anchor['href'])
        # link = "https://www.imdb.com"
        movie_driver.get("https://www.imdb.com"+anchor['href'])
        movie_content=movie_driver.page_source
        movie_soup = BeautifulSoup(movie_content)


        data_div = movie_soup.find("ul",attrs={"class":"TitleBlockMetaData__MetaDataList-sc-12ein40-0"})
        all_lis = data_div.findAll("li")
    

        movie_year = all_lis[0].find("a").text
        duration = all_lis[2].text
        
        print("movie_year",movie_year)
        print("duration",duration)

        desription_span = movie_soup.find("span",attrs={"class":"GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0"})
        description = desription_span.text 
        movie = Movie.objects.create(name=movie_title,rating=rating,release_date=movie_year,duration=duration,description=description)

    except:
        print(a)

movie_driver.quit()
browser.quit()

