from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import sqlite3
import datetime

def main():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("—-incognito")
    options.headless = True
    # DRIVER_PATH = '/Desktop/Webdriver/chromedriver'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    con = sqlite3.connect("ticker_info.db")
    cur = con.cursor()

    curr_date = datetime.date.today().isoformat()
    tickers = ["TSLA", "MSFT", "AMZN", "AAPL", "GOOGL", "NVDA", "META", "IBM"]
    companies = ["tesla", "microsoft", "amazon", "apple", "google", "nvidia", "meta", "IBM"]

    for company, ticker in zip(companies, tickers):
        driver.get(f"https://www.cnbc.com/search/?query={company}")
        time.sleep(random.random()*1.5 + 1)

        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='SearchResult-searchResultImage']")))
        except:
            print('Not properly loaded')

        for _ in range(3):
            driver.execute_script("window.scrollBy(0, 6000);")
            time.sleep(0.5*random.random() + 0.4)
        time.sleep(1)
        data = [(ticker, 'CBNC', curr_date, elt.text) for elt in driver.find_elements(By.XPATH, "//div/a[@class='resultlink']/span[@class='Card-title']")]
        print(data)
        cur.executemany("INSERT INTO all_headlines VALUES(?, ?, ?, ?)", data)
        con.commit()

    con.close()

if __name__ == "__main__":
    main()
