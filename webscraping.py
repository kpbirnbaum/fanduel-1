
from bs4 import BeautifulSoup as bs
import lxml
import requests

raw = requests.get("https://www.espn.com/nba/scoreboard").text

soup = bs(raw,'lxml')
print(soup.prettify())

soup.find('span',)