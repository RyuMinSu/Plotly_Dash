import pandas as pd

from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px


#load
df = pd.read_csv(r'Plotly_Dash\data\medical supplies.csv')
print(df.shape)
print(df.columns)
print(df.head())

df["Part sent date"] = pd.to_datetime(df["Part sent date"]).dt.date #일자
df["Part received date"] = pd.to_datetime(df["Part received date"]).dt.date
df["Prioritize"] = df["Machines"].apply(lambda x:
                                        '⭐⭐⭐' if x > 3000 else (
                                            '⭐⭐' if x > 1000 else (
                                                '⭐' if x > 500 else '')))
print(df.head())



#정의함수
def data_bars(df, column):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)] #.01단위
    print("bounds:", bounds)
    ranges = [
        ((df[column].max() - df[column].min()) * i) + df[column].min()
        for i in bounds
    ] #숫자 찾기
    print("ranges:", ranges)
    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        max_bound_percentage = bounds[i] * 100
        styles.append({
            'if': {
                'filter_query': (
                    '{{{column}}} >= {min_bound}' +
                    (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'background': (
                """
                    linear-gradient(90deg,
                    #0074D9 0%,
                    #0074D9 {max_bound_percentage}%,
                    white {max_bound_percentage}%,
                    white 100%)
                """.format(max_bound_percentage=max_bound_percentage)
            ),
            'paddingBottom': 2,
            'paddingTop': 2
        })

    return styles



#layout
app = Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])

app.layout = dbc.Container(
    [
        html.Div(
            dash_table.DataTable(
                id="mydatatable",
                columns=[                    
                    {'name': 'S/N', 'id': 'Serial number', 'type': 'numeric', 'editable': True},
                    {'name': 'Machines', 'id': 'Machines', 'type': 'numeric', 'editable': False},
                    {'name': 'Country', 'id': 'Country', 'type': 'text', 'editable': True},
                    {'name': 'Part sent date', 'id': 'Part sent date', 'type': 'datetime', 'editable': True},
                    {'name': 'Part received date', 'id': 'Part received date', 'type': 'datetime', 'editable': True},
                    {'name': 'Elapsed Days', 'id': 'Elapsed Days', 'type': 'numeric', 'editable': True},
                    {'name': 'Origin supplier', 'id': 'Origin supplier', 'type': 'text', 'editable': True},
                    {'name': 'Feedback', 'id': 'Feedback', 'type': 'text', 'editable': True},
                    {'name': 'Prioritize', 'id': 'Prioritize', 'type': 'text', 'editable': False},
                ],
                data=df.to_dict("records"),
                style_table={
                    "overflowY": "scroll"
                },
                fixed_columns={"headers":True, "data":1},
                filter_action="native",
                style_data_conditional=[
                    #background
                    {
                        "if": {
                            "filter_query": "{Elapsed Days} > 40 && {Elapsed Days} < 60",
                            "column_id": "Elapsed Days"
                        },
                        "backgroundColor": "hotpink",
                        "color": "white",
                    },
                    {
                        "if": {
                            "filter_query": "{Country} = Canada"
                        },
                        "backgroundColor": "#FFFF00",
                    },
                    #background(blank)
                    {
                        "if": {
                            "filter_query": "{Origin supplier} is blank",
                            "column_id": "Origin supplier"
                        },
                        "backgroundColor": "gray",
                    },
                    #text(bold)
                    {
                        "if":{
                            "filter_query": "{Part sent date} > {Part received date}",
                            "column_id": "Part sent date"
                        },
                        "fontWeight": "bold",
                        "color": "red"
                    },
                    #text(left)
                    {
                        "if": {
                            "column_type": "text"
                        },
                        "textAlign": "left"
                    },
                    #format
                    {
                        "if": {
                            "row_index": 0,
                            "column_id": "Feedback"
                        },
                        "backgroundColor": "purple",
                        "color": "white",
                        "fontWeight": "bold",
                    },
                    #active format
                    {
                        "if": {"state": "active"},
                        "border": "3px solid rgb(0, 116, 217)"
                    },
                    {
                        "if": {"column_editable": True}, 
                        "cursor": "not-allowed", #수정금지표식
                    },
                ] + [
                    #hilight 
                    {
                        "if": {
                            "filter_query": f"{{Machines}} = {i}",
                            "column_id": "Machines"
                        },
                        "backgroundColor": "#7FDBFF",
                        "color": "white",
                    } for i in df['Machines'].nsmallest(3)
                ] + data_bars(df, "Serial number")
                
            ),
            className="six columns"    
        ),

        html.Div(
            dcc.Graph(id="mybar"),
            className='six columns',            
        )
    ],
    className="row"
)





@app.callback(
    Output(component_id='mybar', component_property='figure'),
    Input(component_id='mydatatable', component_property='derived_virtual_data')
)
def table_to_graph(row_data):
    df_table = df if row_data is None else pd.DataFrame(row_data)
    fig = px.bar(df_table, x='Country', y='Machines')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)