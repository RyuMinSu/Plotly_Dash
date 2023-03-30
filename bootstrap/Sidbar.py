import pandas as pd

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px


df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

print(df.shape)
# print(df.columns)
# print(df.head())


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("Number of students per education level", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True, pills=True
        ),
    ], style=SIDEBAR_STYLE
)

content = html.Div(id='page-content', children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output('page-content', 'children'),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1("Kindergarten in Iran", className='text-center'),
            dcc.Graph(
                id="bargraph",
                figure=px.bar(df, barmode="group", x="Years", y=["Girls Kindergarten", "Boys Kindergarten"])
            )
        ]
    elif pathname == "/page-1":
        return  [
            html.H1('Grad School in Iran',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=px.bar(df, barmode='group', x='Years',
                    y=['Girls Grade School', 'Boys Grade School'])
            )
        ]
    elif pathname == "/page-2":
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls High School', 'Boys High School']))
                ]


if __name__=='__main__':
    app.run_server(debug=True, port=3000)