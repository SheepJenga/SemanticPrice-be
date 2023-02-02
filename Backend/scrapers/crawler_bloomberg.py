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
    options.headless = True
    # DRIVER_PATH = '/Desktop/Webdriver/chromedriver'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    con = sqlite3.connect(Settings.get_database())
    cur = con.cursor()

    curr_date = datetime.date.today().isoformat()

    for company, ticker in Settings.get_company_tickers():
        driver.get(f"https://www.nytimes.com/search?query={company}")
        time.sleep(random.random()*1.5 + 1)

        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='search-show-more-button']")))
        except:
            print('Not properly loaded')

        for _ in range(4):
            driver.find_element("xpath", "//button[@data-testid='search-show-more-button']").click()
            time.sleep(0.5*random.random() + 0.3)

        data = [(ticker, 'bberg', curr_date, elt.text) for elt in driver.find_elements(By.XPATH, "//h4[@class='css-2fgx4k']")]
        cur.executemany("INSERT INTO all_headlines VALUES(?, ?, ?, ?)", data)
        con.commit()

    con.close()

if __name__ == "__main__":
    main()
