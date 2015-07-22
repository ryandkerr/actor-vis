# scrape.py
# Ryan Kerr
# scraping IMDB for actor profiles

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re


tom_hanks = "http://www.imdb.com/name/nm0000158/?ref_=nv_sr_1"

def make_soup(url):
  html = urlopen(url).read()
  s = BeautifulSoup(html, "lxml")
  return s

soup = make_soup(tom_hanks)

movies = soup.find_all("div", id=re.compile("^actor-"))
# .find("div", "filmo-category-section")


