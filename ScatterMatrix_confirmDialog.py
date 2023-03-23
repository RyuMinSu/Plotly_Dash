import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import plotly.express as px


df = pd.read_csv(r'Plotly_Dash\data\social_capital.csv')
df.drop(['Alt FIPS Code','FIPS Code','State Abbreviation'], axis=1, inplace=True)

app = dash.Dash(__name__)

# ------------------------------------------------------------------------
app.layout = html.Div([
    dcc.ConfirmDialog(
        id='confirm-dialog',
        displayed=True,
        message='Please choose Dropdown variables!',
    ),

    html.H1("Scatter Matrix of USA Social Capital Project", style={'textAlign':'center'}),

    dcc.Dropdown(
        id='my-dropdown',
        options=[{'label': s, 'value': s} for s in df.columns],
        value=["% children 4+ hours on electronic device past week",
               "% children read to every day past week",
               "% children 4+ hours television past week",
               "% women currently married"],
        multi=True
    ),

    dcc.Graph(id="my-chart", figure={}),
])

if __name__ == "__main__":
    app.run_server(debug=True)