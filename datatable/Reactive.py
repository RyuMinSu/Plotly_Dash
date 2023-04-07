import pandas as pd

from dash import Dash, html, dcc, Input, Output, dash_table, no_update
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


##load
df = px.data.gapminder()

df['id'] = df.index
dff = df[df["year"]==2007]
columns = ["country", "continent", "lifeExp", "pop", "gdpPercap"]
color = {"lifeExp": "#636EFA", "pop": "#EF553B", "gdpPercap": "#00CC96"}
initial_active_cell = {"row": 0, "column": 0, "column_id": "country", "row_id": 0} #초기값


##layout
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H3("2007 Gap Minder", style={"textAlign":"center"}),

                dash_table.DataTable(
                    id="table",
                    columns=[{"name": i, "id": i} for i in columns],
                    data=dff.to_dict('records'),
                    page_size=10,
                    sort_action="native",
                    active_cell=initial_active_cell
                ),
            ],
            className="five columns"
        ),

        html.Div(id="output-graph", className="six columns"),
    ],
    style={"margin":"3rem"},
    className="row"
)

@app.callback(
    Output("output-graph", "children"),
    [Input("table", "active_cell")]
)
def cell_clicked(active_cell):
    if active_cell is None:
        return no_update
    
    row = active_cell["row_id"]
    country = df.at(row, "country")    
    col = active_cell["column_id"]

    y = col if col in ["gdp", "gdpPercap"] else "lifeExp"

    fig = px.line(
        data_frame=df[df["country"]==country],
        x="year",
        y=y,
        title=" ".join([country, y])
    )
    fig.update_layout(
        title={"font_size":20},
        title_x=0.5,
        margin={"t":190, "r":15, "b":5, "l":5}
    )
    fig.update_traces(line={color:color[y]})

    return dcc.Graph(figure=fig)




if __name__ == "__main__":
    app.run_server(debug=True)
