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
	return 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True)
