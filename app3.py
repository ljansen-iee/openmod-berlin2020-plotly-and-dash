import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"

import pandas as pd

heat_demand = pd.read_csv("data/when2heat_stacked_extraction.csv", index_col=[0])
col_options = [dict(label=col.title(), value=col) for col in heat_demand.columns]
arguments = ["x", "y", "color", "facet_col", "facet_row"]

app = dash.Dash(__name__,
    external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Demo: Plotly Express in Dash with Heat Demand Data"),
        html.Div(
            [
                html.P([a + ":", dcc.Dropdown(id=a, options=col_options, value=col_options[0]["value"])])
                for a in arguments
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)

@app.callback(Output("graph", "figure"), [Input(d, "value") for d in arguments])
def make_figure(x, y, color, facet_col, facet_row):
    return px.scatter(
        heat_demand,
        x=x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,
    )

app.run_server(debug=True)
