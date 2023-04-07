import pandas as pd

import plotly.express as px

from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


##load
df = pd.read_excel(r"Plotly_Dash\data\COVID-19-geographic-disbtribution-worldwide-2020-03-29.xlsx")
print(df.head())
dff = df.groupby('countriesAndTerritories', as_index=False)[['deaths','cases']].sum()
print (dff[:5])


##layout
app = Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])

app.layout = dbc.Container(    
    [
        html.P(
            html.H1("Covid19 disbtribution Worldwide"),            
        ),
        html.Div(
            dash_table.DataTable(
                id = "datatable_id",
                data = dff.to_dict('records'),
                columns=[
                    {"name":i, "id":i, "deletable":False, "selectable":False} for i in dff.columns
                ],
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                row_selectable="multi",
                row_deletable=False,
                selected_rows=[],
                page_action="native",
                page_current=0,
                page_size=6,
                fixed_rows={"headers":True, "data":0},
                style_cell_conditional=[                    
                    {"if": {"column_id": "countriesAndTerritories"}, "width":"40%", "textAlign":"left"},
                    {"if": {"column_id": "deaths"}, "width":"30%", "textAlign":"left"},
                    {"if": {"column_id": "cases"}, "width":"30%", "textAlign":"left"},                    
                ],
            )
        ),

        html.Div(
            [
                html.Div(
                    dcc.Dropdown(
                        id="linedropdown",
                        options=[
                            {"label": "Deaths", "value": "deaths"},
                            {"label": "Cases", "value": "cases"}
                        ],
                        value="deaths",
                        multi=False,
                        clearable=False,                        
                    ),
                    className="six columns",
                ),
                html.Div(
                    dcc.Dropdown(
                        id="piedropdown",
                        options=[
                            {"label": "Deaths", "value":"deaths"},
                            {"label": "Cases", "value": "cases"}
                        ],
                        value="cases",
                        multi=False,
                        clearable=True,
                    ),
                    className="six columns",
                ),
            ],
            className="row"
        ),

        html.Div(
            [
                html.Div(
                    dcc.Graph(id="linechart"),
                    className="six columns",
                    ),
                html.Div(
                    dcc.Graph(id="piechart"),
                    className="six columns"
                ),
            ],
            className="row"
        ),
    ]    
)


@app.callback(
    [Output("linechart", "figure"),
     Output("piechart", "figure")],
    [Input("datatable_id", "selected_rows"),
     Input("linedropdown", "value"),
     Input("piedropdown", "value"),]
)
def update_data(chosen_rows, linedropval, piedropval):
    #pie
    if len(chosen_rows) == 0:
        df_filtered = dff[dff["countriesAndTerritories"].isin(["China", "Iran", "Spain", "Italy"])]
    else:
        print(chosen_rows)
        df_filtered = dff[dff.index.isin(chosen_rows)]

    pie_chart = px.pie(
        data_frame=df_filtered,
        names="countriesAndTerritories",
        values=piedropval,
        hole=.3,
        labels={'countriesAndTerritories':'Countries'}
    )

    #line
    list_chosen_countries = df_filtered["countriesAndTerritories"].to_list()
    df_line = df[df["countriesAndTerritories"].isin(list_chosen_countries)]
    
    line_chart = px.line(
        data_frame=df_line,
        x="dateRep",
        y=linedropval,
        color="countriesAndTerritories",
        labels={'countriesAndTerritories':'Countries', 'dateRep':'date'}
    )
    line_chart.update_layout(uirevision="foo")

    return [line_chart, pie_chart]


##run
if __name__ == "__main__":
    app.run_server(debug=True)