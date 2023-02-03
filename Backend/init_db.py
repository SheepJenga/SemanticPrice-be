# ONLY RUN TO INITIALIZE DATABASES!

import sqlite3

con = sqlite3.connect("ticker_info.db")
cur = con.cursor()

query1 = '''CREATE TABLE HEADLINES(
    TICKER CHAR(10), 
    SOURCE CHAR(50), 
    QUERYDATE DATE, 
    HEADLINE TEXT
    )'''

query2 = '''CREATE TABLE SCORES(
    DATE DATE,
    TICKER CHAR(10),
    SOURCE CHAR(30),
    SCORE FLOAT
    )'''


cur.execute(query1)
cur.execute(query2)

con.commit()
con.close()