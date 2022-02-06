from flask import render_template, flash, redirect, request, url_for, jsonify, session, send_from_directory
from v0coderapp import app, db, openai, prefile
from v0coderapp.models import User, Block
import datetime


blocks = [
  
]


@app.route("/", methods=("GET", "POST"))
def hello():
  if request.method == "POST":
    animal = request.form["animal"]
    response = openai.Classification.create(
      search_model="ada",
      model="curie",
      #examples=[
      #["A happy moment", "Positive"],
      #["I am sad.", "Negative"],
      #["I am feeling awesome", "Positive"]
      #,
      file=prefile.id,
      query=animal,
      #labels=["1", "10", "5"],
)
    return redirect(url_for('hello',result=response.label))
  result = request.args.get("result")
  return render_template('home.html', blocks=blocks, utc_dt=datetime.datetime.utcnow(), result=result)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )