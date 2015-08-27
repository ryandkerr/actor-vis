# scrape.py
# Ryan Kerr
# scraping IMDB for actor profiles
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import os

# classifiers for non-movies, not included in scraping
not_movies = ["filming", "pre-production", "post-production", "Short",
              "Mini", "TV", "completed", "announced", "Video"]

# define actors and IMDB urls
actors = {"Harrison Ford": "http://www.imdb.com/name/nm0000148/"}
# "Michael Caine": "http://www.imdb.com/name/nm0000323/?ref_=tt_cl_t4"
# "Chris Pratt": "http://www.imdb.com/name/nm0695435/?ref_=nv_sr_1"
# "Anne Hathaway": "http://www.imdb.com/name/nm0004266/?ref_=nv_sr_1"
# "Morgan Freeman": "http://www.imdb.com/name/nm0000151/?ref_=nv_sr_2"
# "Tom Hanks": "http://www.imdb.com/name/nm0000158/?ref_=nv_sr_1",
# "Jennifer Lawrence": "http://www.imdb.com/name/nm2225369/",

def make_soup(url):
  html = urlopen(url).read()
  s = BeautifulSoup(html, "lxml")
  return s

def get_movie_links(actor_url):
    soup = make_soup(actor_url)
    credits = soup.find_all("div", id=re.compile("^act"))
    movies = []
    for credit in credits:
        movie = True
        for n in not_movies:
            if (movie == False) or (re.search(n, credit.get_text()) != None):
                movie = False
        if movie:
            m = credit.find("a", href=re.compile("/title/")).get("href")
            movies.append("http://www.imdb.com" + m)
    return movies

for actor in actors:
    movies = get_movie_links(actors[actor])
    if not os.path.exists("data/" + actor):
        os.mkdir("data/" + actor)
    for i, movie_link in enumerate(movies):
        with open("data/" + actor + "/" + actor +str(i)+".txt", "wb") as f:
            f.write(urlopen(movie_link).read())
