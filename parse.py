# parse.py
# Ryan Kerr
# parses the downloaded movie pages to create output data

from bs4 import BeautifulSoup
import os
import json

actor_name = "Tom Hanks"


test_file = "data/tom_hanks0.txt"

def make_soup(file_path):
  with open(file_path, "rb") as f:
    html = f.read()
    s = BeautifulSoup(html, "lxml")
    return s

tom0 = make_soup(test_file)

title = tom0.find("span", itemprop="name").get_text()
rating = float(tom0.find("span", itemprop="ratingValue").get_text())
date = tom0.find("meta", itemprop="datePublished").get("content")
genres = tom0.find_all("span", itemprop="genre")
genres = map(lambda x:x.get_text(), genres)
stars = tom0.find("div", itemprop="actors").find_all("span", "itemprop")
stars = map(lambda x:x.get_text(strip=True), stars)
star = True if actor_name in stars else False
gross = tom0.find("h4", text="Gross:").next_sibling.strip()


record = {"title":title, "rating":rating, "date":date,
          "genres":[genre for genre in genres], "star":star, "gross":gross}


# for filename in os.listdir("data"):
#   soup = make_soup(filename)
#   t = soup.find("span", itemprop="name").get_text()
#   r = soup.find("span", itemprop="ratingValue").get_text()
#   d = soup.find("meta", itemprop="datePublished").get("content")
#   g = soup.find_all("span", itemprop="genre")
#   g = map(lambda x:x.get_text(), g)