# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:17:56 2020

@author: Nazibul
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

#hardcoding arrayValues since csv is not provided
arrayValues = ['28.687', '29.687', '24.687', '21.687', '25.687', '28.687']

app = dash.Dash()
app.layout = html.Div([
    html.H1('Title'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Fruit', 'value': 'FRUIT'}
           # {'label': 'Tesla', 'value': 'TSLA'},
           # {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='TEMPERATUR'
    ),
    dcc.Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3,
    ),
    dcc.Graph(id='my-graph', animate=True),
])
#path = "/../example.csv"

#with open(path,"r") as file:
#    reader = csv.reader(file)
#    dataCopy=[]
#    for line in file: 
#        dataCopy.append(line)
#    arrayValues = np.array(dataCopy)



@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):

    return {
        'data': [
                {'y': arrayValues}
            ]
    }

if __name__ == '__main__':
    app.run_server(
    )