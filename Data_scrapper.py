import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/calendar/earnings/"
r = requests.get(url,headers={'User-Agent': 'Custom'})
soup = BeautifulSoup(r.text ,features="lxml")
table = soup.find_all('table')
len(table)

spans = soup.table.thead.find_all('th')
columns = []
for span in spans:
  print(span.text)
  columns.append(span.text)
  
rows = soup.table.tbody.find_all('tr')
len(rows)
stocks_df = pd.DataFrame(columns=columns)
for row in rows:
  elems = row.find_all('td')
  dict_to_add = {}
  for i,elem in enumerate(elems):
    dict_to_add[columns[i]] = elem.text
    stocks_df = stocks_df.append(dict_to_add, ignore_index=True)

print(stocks_df)

#tickerName = input("Enter the stock ticker ")
tsla = yf.Ticker("TSLA")


pd.set_option('display.max_rows', None)
print("Todays PEG ratio " + str(tsla.info['pegRatio'])) # PEG RATIO price/earnings-to-growth
print("Todays PB ratio " + str(tsla.info['currentPrice']/tsla.info['bookValue'])) # PB RATIO Price-to-Book
plt.plot(tsla.history(period='12mo')["Open"] , scalex="Month",scaley="Price")
plt.show()