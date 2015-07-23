# parse.py
# Ryan Kerr
# parses the downloaded movie pages to create output data

from bs4 import BeautifulSoup
import json


test_file = "data/tom_hanks0.txt"

def make_soup(file_path):
  with open(file_path, "rb") as f:
    html = f.read()
    s = BeautifulSoup(html, "lxml")
    return s

tom0 = make_soup(test_file)

t = tom0.find("span", itemprop="name").get_text()
r = tom0.find("span", itemprop="ratingValue").get_text()
d = tom0.find("meta", itemprop="datePublished").get("content")
g = tom0.find_all("span", itemprop="genre")
g = map(lambda x:x.get_text(), g)

record = {"title":t, "rating":r, "date":d, "genres":[genre for genre in g]}