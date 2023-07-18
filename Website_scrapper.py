import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import time
r = requests.get('https://www.capitoltrades.com/trades?assetType=stock')

WebData = BeautifulSoup(r.text, features="lxml")
Hashed = hash(WebData)

while True:
    try:
        time.sleep(20)
        r = requests.get('https://www.capitoltrades.com/trades?assetType=stock')
        WebData = BeautifulSoup(r.text, features="lxml")

        if(Hashed != hash(WebData)):
            print("page updated")
            Hashed = hash(WebData)
            soup = BeautifulSoup(r.text ,features="lxml")
            table = soup.find_all('table')
            len(table)

            spans = soup.table.thead.find_all('span')
            columns = []
            for span in spans:
                columns.append(span.text)
            
            row = soup.table.tbody.find_all('tr')
            stocks_df = pd.DataFrame(columns=columns)

            len(row)
            for rows in row:
                info = rows.find_all('td')
                dict_to_add = {}
                for i, infos in enumerate(info):
                    dict_to_add[columns[i]] = infos.text
                stocks_df = pd.concat([stocks_df,pd.DataFrame(dict_to_add,index=[0])],ignore_index=True)
            
            stocks_df[stocks_df['Published'].filter(like='Today')]
            print(stocks_df.head())



        else:
            continue

    except Exception as err:
        print(err)
        break