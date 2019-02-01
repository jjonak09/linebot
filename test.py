import json
import csv
import random
import re
import requests
# URL = 'https://api.myjson.com/bins/dzzsg'
URL = 'https://youtuberapi.herokuapp.com/api/vtuber/?format=json'
# TEXT = []
read = requests.get(URL)
data = json.loads(read.text)
# TEXT = [
#     "{}はいいぞ!{}".format(data["name"], data["url"]),
#     "{}はいいぞ!{}".format(data["name"], data["url"]),
# ]
# TEXT.append("{}はいいぞ!{}".format(data["name"], data["url"]))
# TEXT.append("{}はいいぞ!{}".format(data["name"], data["url"]))
# TEXT.append(data["name"] + "はいいぞ")
# TEXT.append(data["url"])
id = random.randrange(len(data))
print(data[id])

# tag検索
# https://youtuberapi.herokuapp.com/api/vtuber/?tag=可愛い&format=json
