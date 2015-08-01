# parse.py
# Ryan Kerr
# parses the downloaded movie pages to create output data

from bs4 import BeautifulSoup
import os
import json

# needed for checking if actor is star
actor_name = "Tom Hanks"

def make_soup(file_path):
  with open(file_path, "rb") as f:
    html = f.read()
    s = BeautifulSoup(html, "lxml")
    return s

def de_money(money):
  return money.replace("$", "").replace(",", "").replace("£", "")


movies = []
for filename in os.listdir("data"):
  print(filename)
  soup = make_soup("data/" + filename)
  title = soup.find("span", itemprop="name").get_text()
  rating = float(soup.find("span", itemprop="ratingValue").get_text())
  date = soup.find("meta", itemprop="datePublished").get("content")
  genres = soup.find_all("span", itemprop="genre")
  genres = map(lambda x:x.get_text(), genres)
  stars = soup.find("div", itemprop="actors").find_all("span", "itemprop")
  stars = map(lambda x:x.get_text(strip=True), stars)
  star = True if actor_name in stars else False
  gross = ""
  try: 
    gross = soup.find("h4", text="Gross:").next_sibling.strip() 
  except: 
    gross = "unknown"
  gross = de_money(gross)
  record = {"title":title, "rating":rating, "date":date,
            "genres":[genre for genre in genres], "star":star, "gross":gross}
  movies.append(record)

j = json.dumps(movies)
with open("export/tom_hanks.json", "w") as export:
  print >> export, j