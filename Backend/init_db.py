import sqlite3

con = sqlite3.connect("ticker_info.db")
cur = con.cursor()
cur.execute(f"CREATE TABLE all_headlines(ticker, source, queryDate, headline)")