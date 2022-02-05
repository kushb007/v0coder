from datetime import datetime
from bemo import db


class User(db.Model):
  #id = db.Column(db.Integer, primary_key=True)
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  blocks = db.relationship('Problem', backref='author', lazy=True)

  def __repr__(self):
    return f"User('{self.username}','{self.email}')"

class Block(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  text = db.Column(db.Text, unique=True, nullable=False)
  code = db.Column(db.Text)
  user_id = db.Column(db.String(120), db.ForeignKey('user.id'), nullable=False)
  #user_id = db.Column(db.String, nullable=False)

  def __repr__(self):
    return f"User('{self.title}','{self.date_posted}')"