import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.capitoltrades.com/trades?assetType=stock')

WebData = BeautifulSoup(r.text, features="lxml")
print(WebData)
