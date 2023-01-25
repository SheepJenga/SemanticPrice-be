from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scores.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Thermometers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tckr = db.Column(db.String(10))
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    score = db.Column(db.Float)

    def __init__(self, tckr, score):
        self.tckr = tckr
        self.score = score


# @app.route("/")
# def index():
#     return render_template("index.html", token="Hello Flask + React")

@app.route("/members")
def members():
    return {"members": ["1", "2", "3"]}

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

if __name__ == "__main__":
    app.run(port=8080, debug=True)