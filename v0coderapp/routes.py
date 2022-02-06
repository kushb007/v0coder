from flask import render_template, flash, redirect, url_for, jsonify, session
from v0coderapp import app, db
from v0coderapp.models import User, Block

blocks = [
  
]


@app.route("/")
def hello():
  return render_template('home.html', problems=blocks)