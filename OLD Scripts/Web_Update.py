import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import time
import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv

i=0;

ata=np.genfromtxt('hello.csv',delimiter=',')
Rx=ata[1:,0]
Ry=ata[1:,1]
Rz=ata[1:,2]
Rk=ata[1:,3]
z=len(Rx)
t = np.arange(z) /18000

X = deque(maxlen=36635)
X.append(0)
Y = deque(maxlen=36635)
Y.append(0)
k=1;
def increment(data):  
    global k;
    k=k+1;                                             
    return Rx[k];
items = []
def my_function(x):
  return 5 * x
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_scatter(input):
    X.append(X[-1]+0.025)
    Y.append(increment(items))
   
    

        

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}



if __name__ == '__main__':
    app.run_server(debug=True)