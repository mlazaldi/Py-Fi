#%%
#---------------------------------------------------------------------------------------------------
#IMPORTS
import  pandas              as  pd
import  yfinance            as  yf  

#---------------------------------------------------------------------------------------------------
#VARIABLES
ticker  =   "GC=F"
ticker2 =   "DX-Y.NYB"
start_  =   "2020-01-01"
end_    =   "2023-12-31"


#---------------------------------------------------------------------------------------------------
#pull data from yfinance library 
data            =   yf.download(ticker, start_)
data.reset_index(level=[0],inplace=True)
data.columns    =   data.columns.get_level_values(0)
df              =   data[["Date","Close"]]
df.reset_index(drop=True, inplace=True)
data_dict       =   df.to_dict(orient='records')  #orient='list' or orient='dict' or orient='series' or orient='records' or orient='split' 
print(data_dict)

#%%