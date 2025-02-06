#%%
#---------------------------------------------------------------------------------------------------
#IMPORTS
#import  pandas              as      pd
import  plotly.express      as      px
from    dash                import  Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import  io
from    base64              import b64encode
import  yfinance            as yf  
from    plotly.subplots     import make_subplots


app = Dash(__name__)

buffer = io.StringIO()

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
#data.head(55).style

data2            =   yf.download(ticker2, start_)
data2.reset_index(level=[0],inplace=True)
data2.columns    =   data2.columns.get_level_values(0)
#data2.head(55).style

#---------------------------------------------------------------------------------------------------
#create and display figure
fig     = make_subplots(specs=[[{"secondary_y": True}]])


fig.add_trace(
   px.line  (
                    data
                   ,x                          =   'Date'
                   ,y                          =   'Close'
                   ,markers                    =   False
                   ,color_discrete_sequence    =   ["white"]
               ).data[0]
           ,row=1, col=1
)


#Add the second variable to first chart to the left subplot
fig.add_trace(
   px.line  (
                    data2
                   ,x                           =   'Date'
                   ,y                           =   'Close'
                   ,markers                     =   False
                   ,color_discrete_sequence     =   ["rgb(100, 100, 100)"]
               ).data[0]
               , secondary_y = True
           ,row=1, col=1      
)

fig.update_layout(
                     title_text                 =   f"{ticker} & {ticker2} Price"
                    ,title_font_size            =   30
                    ,width                      =   1000
                    ,height                     =   500
                    ,legend                     =   dict(
                                                    orientation =   "h"
                                                    ,yanchor    =   "bottom"
                                                    ,y          =   1.02
                                                    ,xanchor    =   "right"
                                                    ,x          =   1
                                                )
                    ,paper_bgcolor              =   'rgba(0,0,0,0)'
                    ,plot_bgcolor               =   'rgba(0,0,0,0)'
                )

#display(data)
fig.show()
#%%