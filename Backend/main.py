from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlite3
import os
from scrapers.crawler_settings import Settings

app = Flask(__name__)

today = datetime.date.today().isoformat()

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

@app.route("/api/<string:date>", methods=['GET'])
def all_scores(date):
    con = sqlite3.connect("ticker_info.db")
    cur = con.cursor()
    data = {}
    for source in Settings.get_sources() + ['ALL']:
        res = cur.execute(f"SELECT TICKER, SCORE FROM SCORES WHERE SOURCE='{source}' AND DATE='{date}'")
        source_data = {ticker: score for ticker, score in res.fetchall()}
        data[source] = source_data 
    return data


@app.route("/api/<string:date>/scores/<string:ticker>/<string:source>", methods=['GET'])
def ticker_score(ticker, source, date):
    con = sqlite3.connect("ticker_info.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT SCORE FROM SCORES WHERE TICKER='{ticker}' AND SOURCE='{source}' AND DATE='{date}'")
    score = res.fetchone()
    con.close()
    if score:
        return {'score': score[0]}
    else:
        return {'score': None}


@app.route("/api/<string:date>/headlines/<string:ticker>")
def headlines(ticker):
    # WIP
    pass

if __name__ == "__main__":
    app.run(port=8080, debug=True)