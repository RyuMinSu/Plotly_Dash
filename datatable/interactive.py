from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash(__name__)
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns = [
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        data = df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        column_selectable="single",
        row_selectable='multi',
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_size=10,
        page_current=0,
    ),
    html.Div(id="datatable-interactivity-container")
])

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    Input('datatable-interactivity', 'selected_columns'),
)
def update_style(selected_columns):
    return [
        {'if': {'column_id': i},
         'background_color': '#D2F3FF'} for i in selected_columns
    ]


@app.callback(
    Output('datatable-interactivity-container', 'children'),
    Input('datatable-interactivity', 'derived_virtual_data'),
    Input('datatable-interactivity', 'derived_virtual_selected_rows'),
)
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)
    print(len(dff))

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]
    
    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["country"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color":colors}
                    },
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t":10, "r":10, "l":10,},
                },                
            }
        ) for column in ["pop", "lifeExp", "gdpPercap"] if column in dff
    ]


if __name__ == '__main__':
    app.run_server(debug=True)