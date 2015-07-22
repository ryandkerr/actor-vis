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

def get_movie_links(actor_url):
    soup = make_soup(actor_url)
    credits = soup.find_all("div", id=re.compile("^actor-"))
    movies = []
    for credit in credits:
        movie = True
        for n in not_movies:
            if (movie == False) or (re.search(n, credit.get_text()) != None):
                movie = False
        if movie:
            m = credit.find("a", href=re.compile("/title/")).get("href")
            movies.append("www.imdb.com" + m)
    return movies


tom_movies = get_movie_links(tom_hanks)
