#%%
import math 
import pandas               as pd
import yfinance             as yf
import matplotlib.pyplot    as mp


data                =   yf.download("CNC", start="2023-01-01")
data['SMA20']       =   data['Close'].rolling(window=20).mean()
data['SMA50']       =   data['Close'].rolling(window=50).mean()


to_plot =   ["Close","SMA20","SMA50"]
data[to_plot].plot()
#data.head(55).style
#%%