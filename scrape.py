# scrape.py
# Ryan Kerr
# scraping IMDB for actor profiles
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

# classifiers for non-movies, not included in scraping
not_movies = ["filming", "pre-production", "post-production", "TV", "Short", "Game"]

# define new ones for each actor
actor_page = "http://www.imdb.com/name/nm0000158/?ref_=nv_sr_1"
actor_name = "tom_hanks"


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
            movies.append("http://www.imdb.com" + m)
    return movies

actor_movies = get_movie_links(actor_page)

for i, movie_link in enumerate(actor_movies):
    with open("data/"+actor_name+str(i)+".txt", "wb") as f:
        f.write(urlopen(movie_link).read())
