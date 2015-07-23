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

title = tom0.find("span", itemprop="name").get_text()
rating = tom0.find("span", itemprop="ratingValue").get_text()
year = tom0.find("meta", itemprop="datePublished").get("content")
genres = tom0.find_all("span", itemprop="genre")

# apply the alpha-map technique to convert to .get_text