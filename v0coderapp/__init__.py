from flask import Flask, jsonify, redirect, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from authlib.integrations.flask_client import OAuth
import os
import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = '2a5dbe49dd69e02fe732a038a846977e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
oauth = OAuth(app)
openai.api_key = "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"
#openai.api_key = os.getenv("OPENAI_API_KEY")
prefile = openai.File.create(file=open("alt.jsonl"), purpose="classifications")

from v0coderapp import routes