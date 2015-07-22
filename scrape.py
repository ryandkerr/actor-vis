# scrape.py
# Ryan Kerr
# scraping IMDB for actor profiles

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re


tom_hanks = "http://www.imdb.com/name/nm0000158/?ref_=nv_sr_1"
not_movies = ["filming", "pre-production", "post-production", "TV", "Short", "Game"]

def make_soup(url):
  html = urlopen(url).read()
  s = BeautifulSoup(html, "lxml")
  return s

soup = make_soup(tom_hanks)

credits = soup.find_all("div", id=re.compile("^actor-"))
# .find("div", "filmo-category-section")

movies = []
for credit in credits:
    movie = True
    for n in not_movies:
        if (movie == False) or (re.search(n, credit.get_text()) != None):
            movie = False
    if movie:
        movies.append(credit)



# short = re.search("(TV Short)", movies[5].get_text()) != None

