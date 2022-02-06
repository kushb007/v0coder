from flask import render_template, flash, redirect, url_for, jsonify, session, send_from_directory
from v0coderapp import app, db
from v0coderapp.models import User, Block
import datetime

blocks = [
  
]


@app.route("/")
def hello():
  return render_template('home.html', blocks=blocks, utc_dt=datetime.datetime.utcnow())

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)