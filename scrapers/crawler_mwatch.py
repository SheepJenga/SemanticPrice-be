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
from crawler_settings import Settings

def main():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("—-incognito")
    # options.headless = True
    # DRIVER_PATH = '/Desktop/Webdriver/chromedriver'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    con = sqlite3.connect(Settings.get_database())
    cur = con.cursor()

    curr_date = datetime.date.today().isoformat()
    tickers = ["TSLA", "MSFT", "AMZN", "AAPL", "GOOGL", "NVDA", "META", "IBM"]
    companies = ["tesla", "microsoft", "amazon", "apple", "google", "nvidia", "meta", "IBM"]

    for company, ticker in Settings.get_company_tickers():
        driver.get(f"https://www.marketwatch.com/search?q={company}&ts=0&tab=All%20News")
        time.sleep(random.random()*1.5 + 1)

        try:
            # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@class='close-btn']")))
            time.sleep(2)
        except:
            print('Not properly loaded')
        driver.find_element("xpath", "//button[@class='close-btn']").click()
        time.sleep(0.5*random.random() + 1)
        driver.find_element("xpath", "//button[@class='btn btn--secondary js--more-headlines-site-search']").click()

        data = [(ticker, 'mwatch', curr_date, elt.text) for elt in driver.find_elements(By.XPATH, "//h3/a[@class='link']")]
        print(data)
        # cur.executemany("INSERT INTO all_headlines VALUES(?, ?, ?, ?)", data)
        # con.commit()

    con.close()

if __name__ == "__main__":
    main()
