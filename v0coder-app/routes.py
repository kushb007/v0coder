from flask import render_template, flash, redirect, url_for, jsonify, session
from bemo import app, db
from bemo.models import User, Blocks

blocks = [
  
]


@app.route("/")
def hello():
  return render_template('home.html', problems=blocks)