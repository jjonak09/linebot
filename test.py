import json
import csv
import random
import re
import requests
URL = 'https://api.myjson.com/bins/dzzsg'

read = requests.get(URL)
data = json.loads(read.text)
print(str(data["name"]) + "はいいぞ")
print(data["url"])
