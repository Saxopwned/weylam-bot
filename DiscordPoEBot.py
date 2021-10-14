# All-inclusive PoE Bot
import requests
import os
from html.parser import HTMLParser

URL = ("https://poedb.tw/us/Leap_Slam")
page = requests.get(URL)

# print(page.text)

# with open("Leap_Slam.HTML", "w+", encoding="utf-8"):