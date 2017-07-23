import os, json, requests
import sys, time
import urllib, urllib2
import json

from flask import Flask, request
from flask import render_template

from flask_heroku import Heroku

TOKEN = '351697767:AAFV5Y2RewXLLXGbcGohE7reo3O1-lb0LpU'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/webhook", methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)
	update_id = data['update_id']
        try:
            message = data['message']
        except:
            message = data['edited_message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        def reply(msg=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            else:
                logging.error('no msg specified')
                resp = None

            log('send response:')
            log(resp)

        if text.startswith('/'):
            if text == '/start':
                reply('Bot enabled')
                setEnabled(chat_id, True)
            elif text == '/stop':
                reply('Bot disabled')
                setEnabled(chat_id, False)
            else:
                reply('What command?')

        # CUSTOMIZE FROM HERE

        elif 'who are you' in text:
            reply('I am Igt Bot')
        elif 'what time' in text:
            reply('look at the corner of your screen!')
        else:
            reply('I got your message! (but I do not know how to answer)')
	return "ok", 200



def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True)
