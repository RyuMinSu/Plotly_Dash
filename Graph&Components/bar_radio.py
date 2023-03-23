import pandas as pd

import datetime as dt

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import plotly.express as px



df = pd.read_csv(r"Plotly_Dash\data\Urban_Park_Ranger_Animal_Condition_Response.csv")

#컬럼값 확인
# print('\tAge values')
# print(df['Age'].value_counts(dropna=False))
# print('\n\t# of Animals values')
# print(df['# of Animals'].value_counts(dropna=False))

"""
1. # of Animals: 0초과 제외(null도 함께 사라짐)
2. Age: Multiple 제외

3. Month of Initial Call 컬럼 추가: Date and Time of initial call: 월만 남기기

4. Amount of Animals 컬럼 추가: # of Animals
5. Time Spent on Site (hours) 컬럼 추가: Duration of Response
"""

###1, 2
cond1 = df['# of Animals'] > 0
cond2 = df['Age'] != 'Multiple'
df = df[(cond1)&(cond2)]
# 컬럼값 확인
# print('\tAge values')
# print(df['Age'].value_counts(dropna=False))
# print('\n\t# of Animals values')
# print(df['# of Animals'].value_counts(dropna=False))

###3
df["Month of Initial Call"] = pd.to_datetime(df["Date and Time of initial call"])
df["Month of Initial Call"] = df["Month of Initial Call"].dt.strftime("%m")

###4, 5
df["Amount of Animals"] = df["# of Animals"]
df["Time Spent on Site (hours)"] = df["Duration of Response"]

# print(df.shape, df.columns)

# 레이아웃 -----------------------------------------------------------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        html.Pre(
            children= "NYC Calls for Animal Rescue",
            style={"text-align": "center", "font-size": "100%", "color": "black"},
        )
    ),
    html.Div([
        html.Label(
            ['X-axis categories to compare:'],
            style={"font-weight": "bold"},
        ),
        dcc.RadioItems(
            id='xaxis_raditem',
            options=[
                {'label': "Month Call Made", "value": "Month of Initial Call"},
                {'label': 'Animal Health', 'value': 'Animal Condition'},
            ],
            value= 'Animal Condition',
            style={"width": "50%"}
        )
    ]),
    html.Div([
        html.Br(),
        html.Label(
            ['Y-axis values to compare:'],
            style={'font-weight': 'bold'}
        ),
        dcc.RadioItems(
            id = 'yaxis_raditem',
            options=[
                {'label': 'Time Spent on Site (hours)', 'value': 'Time Spent on Site (hours)'},
                {'label': 'Amount of Animals', 'value': 'Amount of Animals'},
            ],
            value = 'Time Spent on Site (hours)',
            style={"width": "50%"}
        )
    ]),
    html.Div(
        dcc.Graph(id='the_graph')
    ),
])



# callback ---------------------------------------------------------------------------

@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)
def update_graph(x_axis, y_axis):
    dff = df

    barchart = px.bar(
        data_frame=dff,
        x=x_axis,
        y=y_axis,
        title = y_axis + ": by " + x_axis,
        facet_col='Borough',        
        color='Borough',
        # barmode='group',
    )
    return (barchart)


if __name__ == "__main__":
    app.run_server(debug=True)



