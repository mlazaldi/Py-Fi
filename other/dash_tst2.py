#%%
import  pandas                  as      pd
# import  psycopg2                as      db
import  plotly.express          as      px  # (version 4.7.0 or higher)
import  plotly.graph_objects    as      go
#from    common                  import  no_phi_db_connect
from    dash                    import  Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import  yfinance                as yf  
from    plotly.subplots         import make_subplots


app = Dash(__name__)
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
#app layout
app.layout = html.Div([

    html.H1("Proof of Concept", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options   =    [
                                     {"label": "2020", "value": 2020}
                                    ,{"label": "2021", "value": 2021}
                                    ,{"label": "2022", "value": 2022}
                                    ,{"label": "2023", "value": 2023}
                                    ,{"label": "2024", "value": 2024}
                                ]
                 ,multi     =   False
                 ,value     =   2024
                 ,style     =   {'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='transactions_graph', figure={})

])



#---------------------------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        Output(component_id='output_container', component_property='children'),
        Output(component_id='transactions_graph', component_property='figure')
    ],
    [Input(component_id='slct_year', component_property='value')]
    )
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)
    # update the slicer
    df_copy = data.copy()
    df_copy = df_copy[df_copy["Date"] == option_slctd]


    # Plotly Express build figure
    fig =   px.line(
                    data_frame  =   df_copy
                    ,x          =   'Date'
                    ,y          =   'Close'
                )
    
#    fig.update_layout(
#                    title_font_size     =   30
#                    #,font_family        =   "Courier New"
#                    ,title_font_family  =   "Courier New"
#                    ,title_font_color   =   "white"
#                )

    return container, fig



#---------------------------------------------------------------------------------------------------
#?????
if __name__ == '__main__':
    app.run_server(debug=True)
# %%