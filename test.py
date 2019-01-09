import json
import csv
import random
import re
import requests
URL = 'https://api.myjson.com/bins/dzzsg'
TEXT = []
read = requests.get(URL)
data = json.loads(read.text)
TEXT.append(data["name"] + "はいいぞ")
TEXT.append(data["url"])
print(TEXT[0])
