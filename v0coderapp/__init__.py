from flask import Flask, jsonify, redirect, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = '2a5dbe49dd69e02fe732a038a846977e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
oauth = OAuth(app)

from v0coderapp import routes