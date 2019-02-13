from flask import Flask, request, abort, make_response, jsonify
import os
import requests
import json
import csv
import random
import re

app = Flask(__name__)

URL = 'https://youtuberapi.herokuapp.com/api/'
JSON_TYPE = '?format=json'
Youtube_URL = 'https://www.youtube.com/channel/'


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]
    if intent["displayName"] == "recommand_youtuber":
        data = get_data_from_api(req)
        res = make_mes_recommand_youtuber(data)
    elif intent["displayName"] == "take_new_video":
        res = get_new_video(req)

    return make_response(jsonify({'fulfillmentText': res}))


def get_data_from_api(req):
    params = req["queryResult"]["parameters"]
    if params["youtuber_vtuber"] == 'Vtuber':
        url = URL + 'vtuber/' + JSON_TYPE
    elif params["youtuber_vtuber"] == 'Youtuber':
        url = URL + 'youtuber/' + JSON_TYPE
    if params["youtuber_tag"] != "":
        url = url + '&tag=' + params["youtuber_tag"]
    if params["belonging_agency"] != "":
        url = url + '&belong=' + params["belonging_agency"]
    read = requests.get(url)
    data = json.loads(read.text)
    return data


def get_new_video(req):
    params = req["queryResult"]["parameters"]
    url = URL + 'vtuber/' + JSON_TYPE + '&name=' + params["any"]
    read_api = requests.get(url)
    get_youtuber_data = json.loads(read_api.text)
    # read_youtube_api = requests.get(
    #     'https://www.googleapis.com/youtube/v3/search?part=id&channelId=' + get_youtuber_data["channel_id"] + '&order=date&key=AIzaSyDhjFEKpgj1BNY9gqbbz8zpao1U5-mn3jU')
    # get_video_id = json.loads(read_youtube_api.text)
    # video_id = get_video_id["items"][1]["id"]["videoId"]
    return get_youtuber_data["name"]


def make_mes_recommand_youtuber(data):
    id = random.randrange(len(data))
    res = "{}はいいぞ! {}".format(
        data[id]["name"], Youtube_URL + data[id]["channel_id"])
    return res


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
