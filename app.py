import os, json, requests
import sys, time
import urllib

from flask import Flask, request, redirect, url_for, flash
from flask import render_template

from flask_heroku import Heroku


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True)
