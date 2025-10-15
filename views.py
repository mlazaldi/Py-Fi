#%%
from    flask       import  Blueprint, render_template, jsonify, redirect, url_for, send_from_directory
import  subprocess
from    dash        import  Dash
import  sys
import  os
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

views    =   Blueprint(__name__, "views")


@views.route("/",endpoint='one')
def home():
    return render_template("index.html")


@views.route("/chartjs",endpoint='two')
def chart_js():
    return render_template("graph.html")

    
@views.route('/data',endpoint='three')
def data():
        import  pandas              as  pd
        import  yfinance            as  yf  
        import  time

        #---------------------------------------------------------------------------------------------------
        #VARIABLES
        ticker  =   "SI=F"
        start_  =   "2024-01-01"
        ticker2 =   "DX-Y.NYB"
        end_    =   "2023-12-31"


        #---------------------------------------------------------------------------------------------------
        #pull data from yfinance library 
        data            =   yf.download(ticker, start_)
        data.reset_index(level=[0],inplace=True)
        data.columns    =   data.columns.get_level_values(0)
        df              =   data[["Date","Close"]]
        df.reset_index(drop=True, inplace=True)
        data_dict       =   df.to_dict(orient='records')
        time.sleep(2) 
        return jsonify(data_dict)


@views.route("/plotly",endpoint='four')
def chart_js():
    return render_template("graph2.html")


#  TESTING ---------------------------------------------------------------------------------------------------
# @views.route("/plotly",endpoint='five')
# def render_dashboard():
#     return redirect('/pathname')  # Redirect to Dash app


# %%