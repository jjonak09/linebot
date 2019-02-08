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
    data = get_data_from_api(req)
    res = make_message(data)
    return make_response(jsonify({'fulfillmentText': res}))


　


def get_data_from_api(req):

    params = req["queryResult"]["parameters"]

    # youtuber or vtuber
    if params["youtuber_vtuber"] == 'Vtuber':
        url = URL + 'vtuber/' + JSON_TYPE
    elif params["youtuber_vtuber"] == 'Youtuber':
        url = URL + 'youtuber/' + JSON_TYPE

    # tagでフィルタリング
    if params["youtuber_tag"] != "":
        url = url + '&tag=' + params["youtuber_tag"]

    # 所属事務所でフィルタリング
    if params["belonging_agency"] != "":
        url = url + '&belong=' + params["belonging_agency"]

    read = requests.get(url)
    data = json.loads(read.text)

    return data


def make_message(data):
    id = random.randrange(len(data))
    res = "{}はいいぞ! {}".format(
        data[id]["name"], Youtube_URL + data[id]["channel_id"])
    return res


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
