from nltk.sentiment import SentimentIntensityAnalyzer
import datetime
import sqlite3
from scrapers.crawler_settings import Settings

def analyze():
    con = sqlite3.connect("ticker_info.db")
    cur = con.cursor()
    today = datetime.date.today()

    done_query1 = f"SELECT SCORE FROM SCORES WHERE DATE='{today}'"
    # done_query2 = f"SELECT headline FROM all_headlines WHERE queryDate='{today}'"
    if cur.execute(done_query1).fetchone():
        con.close()
        return None

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

    return 'Data fetched successfully'

if __name__ == '__main__':
    analyze()
