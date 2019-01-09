# インポートするライブラリ
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
import os
import requests
import json
import csv
import random
import re

app = Flask(__name__)

# 環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
# 環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

URL = 'https://api.myjson.com/bins/dzzsg'


def get_answer():
    url = URL
    read = requests.get(URL)
    data = json.loads(read.text)
    return data


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# MessageEvent


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    TEXT = []
    line_answers = get_answer()
    TEXT.append("{}はいいぞ!".format(line_answers["name"]))
    TEXT.apeend(line_answers["url"])
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=TEXT[0])
    )
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=TEXT[1])
    # )


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
