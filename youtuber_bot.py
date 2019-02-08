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
    res = make_message(req)
    return make_response(jsonify({'fulfillmentText': res}))


def make_message(req):
    params = req['queryResult']['parameters']

    if params['youtuber_vtuber'] == 'Vtuber':
        url = URL + 'vtuber/' + JSON_TYPE
    else if params['youtuber_vtuber'] == 'Youtuber':
        url = URL + 'youtuber/' + JSON_TYPE

    # if params['youtuber_tag'] != "":
    #     url = url + '&tag=' + params['youtuber_tag']

    return 'hello'


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
