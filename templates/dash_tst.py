#%%
#---------------------------------------------------------------------------------------------------
#IMPORTS
from    dash                    import  Dash, dcc, html, Input, Output, State 
import  yfinance                as      yf  
import  plotly.graph_objs       as      go 
# import  streamlit               as      st


dash_app = Dash()


#---------------------------------------------------------------------------------------------------
#HTML LAYOUT
dash_app.layout  =   html.Div(
                        style={'backgroundColor': '#111111', 'color': '#FFFFFF', 'padding': '20px'},
                        
                        children=[
                                    html.H1(children="Stock candlestick chart tool", style={'textAlign': 'center', 'color': '#FFFFFF'}),

                                    html.Div(children=[
                                            html.Label(children='Enter Stock Ticker Symbol:', style={'color': '#FFFFFF'}),
                                            dcc.Input(id='ticker-input', type='text', value='GC=F',
                                                    style={'backgroundColor': '#333333', 'color': '#FFFFFF'})
                                            ], style={'padding': '10px'}),

                                    html.Div(children=[
                                            html.Label(children='Select start date:', style={'color': '#FFFFFF'}),
                                            dcc.DatePickerSingle(id='start-date-picker', date='2020-01-01')
                                            ], style={'padding': '10px'}),

                                    html.Div(children=[
                                            html.Label(children='Select end date:', style={'color': '#FFFFFF'}),
                                            dcc.DatePickerSingle(id='end-date-picker', date='2025-01-01')
                                            ], style={'padding': '10px'}),

                                    html.Div(children=[
                                            html.Button(children='Submit', id='submit-button', n_clicks=0, style={'backgroundColor': '#444444', 'color': '#FFFFFF'})
                                            ], style={'padding': '10px', 'textAlign': 'center'}),

                                    html.Div(id='chart-container', style={'visibility': 'hidden'}, children=[
                                            dcc.Graph(id='candlestick-chart',style={'backgroundColor': '#111111'})
                                            ])
                                ]
                        )


#---------------------------------------------------------------------------------------------------
#INTERACTIVE FUNCTIONALITY
@dash_app.callback(
                [  
                    Output(component_id ='candlestick-chart' , component_property   = 'figure'),
                    Output(component_id ='chart-container'   , component_property   = 'style')
                ],
                [
                    Input(component_id ='submit-button'     , component_property    = 'n_clicks')
                ],
                [
                    State(component_id ='ticker-input'      , component_property    = 'value'),
                    State(component_id ='start-date-picker' , component_property    = 'date'),
                    State(component_id ='end-date-picker'   , component_property    = 'date')
                ]
            )

def update_chart(n_clicks, ticker, start_date, end_date):
    if n_clicks > 0:
        df              =   yf.download(ticker, start=start_date, end=end_date,)
        df.columns      =   df.columns.get_level_values(0)
        symb            =   yf.Ticker(ticker)
        company_name    =   symb.info.get("longName", ticker)

        fig = go.Figure(data=[go.Candlestick(
                                                 x       =   df.index
                                                ,open    =   df['Open'  ]
                                                ,close   =   df['Close' ]
                                                ,high    =   df['High'  ]
                                                ,low     =   df['Low'   ]
                                            )
                                ]
                        )

        fig.update_layout(
             title                      =   f'Candlestick Char of "{company_name}"'
            ,xaxis_title                =   'Date'
            ,yaxis_title                =   'Price (USD)'
            ,xaxis_rangeslider_visible  =   False
            ,template                   =   'plotly_dark'    
            ,yaxis                      =   dict(tickformat=",",tickprefix='$')  # Add dollar sign as prefix
            ,xaxis                      =   dict(tickformat="%b %Y") # Display abbreviated month and year
        )

        return fig, {'visibility': 'visible'}
    return go.Figure(), {'visibility': 'hidden'}


if __name__ == '__main__':
    dash_app.run(debug=True)

#%%