import os, json, requests
import sys, time
import urllib, urllib2
import json

from flask import Flask, request
from flask import render_template

from flask_heroku import Heroku
data

TOKEN = '351697767:AAFV5Y2RewXLLXGbcGohE7reo3O1-lb0LpU'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/set_webhook")
def set_webhook():
	url = "https://stark-badlands-91912.herokuapp.com"
	data = json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url}))))
	print data
	return requests.post(data)
def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True)
