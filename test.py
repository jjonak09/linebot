import json
import csv
import random
import re
import requests
URL = 'https://api.myjson.com/bins/dzzsg'
# TEXT = []
read = requests.get(URL)
data = json.loads(read.text)
TEXT = "{}はいいぞ!".format(data["name"])
# TEXT.append(data["name"] + "はいいぞ")
# TEXT.append(data["url"])
print(TEXT)
