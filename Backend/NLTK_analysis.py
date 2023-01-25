from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3

con = sqlite3.connect("ticker_info.db")
cur = con.cursor()

res = cur.execute("SELECT headline FROM all_headlines where \
    ticker='META' and source='wsj' and queryDate='2023-01-10'")

sia = SentimentIntensityAnalyzer()
run_sum = 0
headlines = res.fetchall()
for headline in headlines:
    run_sum += sia.polarity_scores(headline[0])['compound']
print(run_sum/len(headlines))