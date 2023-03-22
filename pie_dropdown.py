import pandas as pd

import dash
from dash.dependencies import Input, Output
from dash import html, dcc

import plotly.express as px

df = pd.read_csv(r"Plotly_Dash\data\Urban_Park_Ranger_Animal_Condition_Response.csv")

print(df.columns)


app = dash.Dash(__name__)

app.layout = html.Div([
    #1단
    html.Div([
        html.Label(["NYC Calls for Animal Rescue"]),
        dcc.Dropdown(
            id='my_dropdown',
            #label에 정하고 싶은 컬럼명 / value에 원래 컬럼명
            options=[
                {'label': 'Action Taken by Ranger', 'value': 'Final Ranger Action'},
                {'label': 'Age', 'value': 'Age'},
                {'label': 'Animal Health', 'value': 'Animal Condition'},
                {'label': 'Borough', 'value': 'Borough'},
                {'label': 'Species', 'value': 'Animal Class'},
                {'label': 'Species Status', 'value': 'Species Status'}
            ],
            value='Final Ranger Action',
            multi=False,
            clearable=False,
            style={'width': '50%'},
        )
    ]),

    #2단
    html.Div([
        html.Div([
            dcc.Graph(id='the_graph1')
        ], style={"flex":1}),
        html.Div([
            dcc.Graph(id='the_graph2')
        ], style={"flex":1}),
    ], style={
        "display":"flex",
        "flex-direction":"row",
    }),
])



# callback-----------------------------------------------------------------

@app.callback(
    Output(component_id='the_graph1', component_property='figure'),
    Output(component_id='the_graph2', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),]
)
def update_graph(my_dropdown):
    dff = df
    piechart = px.pie(
        data_frame=dff, #df
        names=my_dropdown, #컬럼명
        hole=.5, #홀크기
    )
    return [piechart, piechart]


if __name__ == '__main__':
    app.run_server(debug=True)