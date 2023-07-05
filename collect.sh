#!/bin/bash

cd scrapers

echo "scraping barrons"
python3 crawler_barrons.py

echo "scraping bloomberg"
python3 crawler_bloomberg.py

echo "scraping cbnc"
python3 crawler_cbnc.py

echo "scraping wsj"
python3 crawler_wsj.py

echo "scraping yahoo"
python3 crawler_yahoo.py
