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

line_bot_api = LineBotApi('b7fd7d68bd7164f2a2b9e19f2888b2f8')
handler = WebhookHandler('yVq8w7bq0Ha0CVFFAAr6DPlNU2nBIxziSUJ+Z/OXDeuysnQA39pxGuqwpXkignp+E4C+nIna9Dt/FbtbOiWFoXXGz+yFA6k8V3leqeD506+kZjxXgnyaoblFX8RVANbpYJVgjViO9HEOUYOqde7tbAdB04t89/1O/w1cDnyilFU=')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
        message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
