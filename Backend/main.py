from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlite3
import os

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticker_info.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# class Thermometers(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tckr = db.Column(db.String(10))
#     date = db.Column(db.DateTime, default=datetime.datetime.now)
#     score = db.Column(db.Float)

#     def __init__(self, tckr, score):
#         self.tckr = tckr
#         self.score = score


@app.route("/")
def index():
    con = sqlite3.connect("./Backend/ticker_info.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM all_headlines WHERE ticker='AMZN'")
    # print()
    # return render_template("index.html", token="Hello Flask + React")
    # con.close()
    return {"hi": res.fetchone(), "hi2": "'"}

@app.route("/scores")
def members():
    return {'tesla': 0.49, 'amazon': 0.2, 'google': 0.35, 'microsoft': 0.23}

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

if __name__ == "__main__":
    app.run(port=8080, debug=True)