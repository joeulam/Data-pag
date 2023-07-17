import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from bs4 import BeautifulSoup
r = requests.get("https://finance.yahoo.com/quote/ISEE/analysis",headers={'User-Agent': 'Custom'})
tsla = yf.Ticker("ISEE")
soup = BeautifulSoup(r.text ,features="lxml")
table = soup.find_all('tbody')
len(table[2])
spans = soup.table.find_all('tr')
columns = []
for span in spans:
  columns.append(span.text)

delimiter = '-'
newList = [delimiter+x for x in columns[5].split(delimiter) if x]


pd.set_option('display.max_rows', None)
print("Todays PEG ratio " + str(tsla.info['pegRatio'])) # PEG RATIO price/earnings-to-growth
print("Todays PB ratio " + str(tsla.info['currentPrice']/tsla.info['bookValue'])) # PB RATIO Price-to-Book
print("Todays PE ratio " + str(tsla.info['currentPrice']/float(newList[4]))) # PB RATIO Price-to-Book

