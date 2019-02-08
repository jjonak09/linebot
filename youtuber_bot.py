from flask import Flask, request, abort, make_response, jsonify
import os
import requests
import json
import csv
import random
import re

app = Flask(__name__)

URL = 'https://youtuberapi.herokuapp.com/api/vtuber/'
JSON = 'format=json'
Youtube_URL = 'https://www.youtube.com/channel/'


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    return make_response(jsonify({'fullfillmentText': 'hello'}))
