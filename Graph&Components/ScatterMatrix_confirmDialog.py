import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import plotly.express as px


df = pd.read_csv(r'Plotly_Dash\data\social_capital.csv')
df.drop(['Alt FIPS Code','FIPS Code','State Abbreviation'], axis=1, inplace=True)
print(df.head())

app = dash.Dash(__name__)

# ------------------------------------------------------------------------
app.layout = html.Div([
    dcc.ConfirmDialog(
        id='confirm-dialog',
        displayed=False,
        message='Please choose Dropdown variables!',
    ),

    html.H1("Scatter Matrix of USA Social Capital Project", style={'text-align':'center'}),

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

# callback -----------------------------------------------------------------
@app.callback(
    Output(component_id='confirm-dialog', component_property='displayed'),
    Output(component_id='my-chart', component_property='figure'),
    Input(component_id='my-dropdown', component_property='value')
)
def update_graph(dpdn_val):
    if len(dpdn_val) > 0:
        fig = px.scatter_matrix(df, dimensions=dpdn_val, color='population',
                                hover_data={'State':True, 'population':':,'})
        
        fig.update_traces(diagonal_visible=False, showupperhalf=False, showlowerhalf=True)
    return False, fig

if __name__ == "__main__":
    app.run_server(debug=True)