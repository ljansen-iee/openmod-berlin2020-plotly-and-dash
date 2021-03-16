import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
        html.H1("Demo: Plotly Express in Dash with Heat Demand Data"),
        dcc.Input(id="x"),
        html.H2(id="x_output")

    ])

@app.callback(Output("x_output", "children"), [Input("x", "value")])
def cb(x):
    return x

app.run_server(debug=True)