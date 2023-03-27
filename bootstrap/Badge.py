"""
구성요소 사용 상황별 피드백 메세지

"""

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.Badge("Primary", color="primary", className="me-1"),
        dbc.Badge("Secondary", color="secondary", className="me-1"),
        dbc.Badge("Success", color="success", className="me-1"),
        dbc.Badge("Warning", color="warning", className="me-1"),
        dbc.Badge("Danger", color="danger", className="me-1"),
        dbc.Badge("Info", color="info", className="me-1"),
        dbc.Badge("Light", text_color="dark", color="light", className="me-1"),
        dbc.Badge("Dark", color="dark"),
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)