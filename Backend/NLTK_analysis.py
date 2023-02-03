from nltk.sentiment import SentimentIntensityAnalyzer
import datetime
import sqlite3
from scrapers.crawler_settings import Settings

con = sqlite3.connect("ticker_info.db")
cur = con.cursor()
today = datetime.date.today()
dates = [today.isoformat(), 
        (today - datetime.timedelta(days=1)).isoformat(), 
        (today - datetime.timedelta(days=2)).isoformat()]
sia = SentimentIntensityAnalyzer()

for company, ticker in Settings.get_company_tickers():
    all_sum = 0
    for source in Settings.get_sources():
        sub_sum = 0
        sub_count = 0

        for date in dates:
            query = f"SELECT headline FROM all_headlines WHERE ticker='{ticker}' and source='{source}' and queryDate='{date}'"
            res = cur.execute(query)
            headlines = res.fetchall()
            sub_count += len(headlines)
            for headline in headlines:
                sub_sum += sia.polarity_scores(headline[0])['compound']
        if sub_count:
            cur.execute("INSERT INTO SCORES VALUES(?, ?, ?, ?)", (today, ticker, source, sub_sum/sub_count))
            all_sum += (sub_sum/sub_count)
    cur.execute("INSERT INTO SCORES VALUES(?, ?, ?, ?)", (today, ticker, 'ALL', all_sum/len(Settings.get_sources())))

con.commit()
con.close()