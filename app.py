from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('HdawsI3lohTlPNZVemNEhX1qHzJNWKmqMtSrdPQNaUNxlwA4quPIvcpJb+19O3djUwDSGiBX5R32Z772HzEFQHOfFpldF3W0peLrwfSdRVGY2v7q4UOQ0TS668IHpZDvLbRqek+1+qUhUvb2Ni4flQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('875d85aeac92f9c43141ac9bd080e2f0')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text
	r = '很抱歉，你說什麼'

    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
    	r = '我是機器人'
    elif '訂位' in msg:
    	r = '您想訂位，是嗎？'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()