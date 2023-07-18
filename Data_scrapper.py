import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/most-active/"
r = requests.get(url,headers={'User-Agent': 'Custom'})
soup = BeautifulSoup(r.text ,features="lxml")
table = soup.find_all('table')
len(table)

spans = soup.table.thead.find_all('th')
columns = []
for span in spans:
  columns.append(span.text)
  
rows = soup.table.tbody.find_all('tr')
len(rows)
stocks_df = pd.DataFrame(columns=columns)
for row in rows:
  elems = row.find_all('td')
  dict_to_add = {}
  for i,elem in enumerate(elems):
    dict_to_add[columns[i]] = elem.text
  stocks_df = pd.concat([stocks_df, pd.DataFrame(dict_to_add, index=[0])], ignore_index=True)

stocks_df = stocks_df.sort_values(by='Volume')
print(stocks_df.head(10))
top10 = stocks_df['Symbol'].head(10)
top10List = []
for i in top10:
  top10List.append(i)

#tickerName = input("Enter the stock ticker ")


print(top10List)
for i in range (2):
  for j in range (5):
    tsla = yf.Ticker(top10List[i*2+j])
    plt.plot(tsla.history(period='6mo')["Open"], label = str(top10List[i*2+j]))
    plt.ylabel("Market Opening Price")
    plt.xlabel("6 Month View")
    plt.title("Top 10 Stock By Market Volume")
plt.legend(loc=3)
plt.show()

