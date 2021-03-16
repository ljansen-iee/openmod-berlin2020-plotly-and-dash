import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

heat_demand = pd.read_csv("data/when2heat_stacked_extraction.csv", index_col=[0])
col_options = [dict(label=col.title(), value=col) for col in heat_demand.columns]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Demo: Plotly Express in Dash with Heat Demand Data"),
    dcc.Dropdown(id="x", options=col_options, value=col_options[0]["value"]),
    dcc.Graph(id="graph", figure=px.scatter())
])

@app.callback(Output("graph", "figure"), [Input("x", "value")])
def cb(x):
    return px.scatter(heat_demand, x=x)

app.run_server(debug=True)