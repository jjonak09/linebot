import json
import csv
import random
import re
import requests
# URL = 'https://api.myjson.com/bins/dzzsg'
URL = 'https://youtuberapi.herokuapp.com/api/vtuber/?format=json'
# TEXT = []
# read = requests.get(URL)
# data = json.loads(read.text)
# TEXT = [
#     "{}はいいぞ!{}".format(data["name"], data["url"]),
#     "{}はいいぞ!{}".format(data["name"], data["url"]),
# ]
# TEXT.append("{}はいいぞ!{}".format(data["name"], data["url"]))
# TEXT.append("{}はいいぞ!{}".format(data["name"], data["url"]))
# TEXT.append(data["name"] + "はいいぞ")
# TEXT.append(data["url"])
# id = random.randrange(len(data))
# print(data[id])

# tag検索
# https://youtuberapi.herokuapp.com/api/vtuber/?tag=可愛い&format=json
# get_channel_id = "UC4YaOt1yT-ZeyB0OmxHgolA"

# read_youtube_api = requests.get(
#     'https://www.googleapis.com/youtube/v3/search?part=id&channelId=' + get_channel_id + '&order=date&key=AIzaSyDhjFEKpgj1BNY9gqbbz8zpao1U5-mn3jU')
# data = json.loads(read_youtube_api.text)
# print(data["items"][1]["id"]["videoId"])
url = 'https://youtuberapi.herokuapp.com/api/vtuber/?format=json&name=キズナアイ'
read_youtube_api = requests.get(url)
data = json.loads(read_youtube_api.text)
print(data[0]["name"])
