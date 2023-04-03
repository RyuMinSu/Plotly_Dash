from dash import Dash, html, dcc, ctx, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px


data_canada = px.data.gapminder().query("country == 'Canada'")
print(data_canada)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

buttons = html.Div(
    [
        dbc.Button("Bar Chart", id="btn-bar", color="primary"),
        dbc.Button("Line Chart", id="btn-line", color="secondary"),
        dbc.Button("Area Chart", id="btn-area", color="warning"),
    ],
    className='d-grid gap-2'
)

app.layout = dbc.Container(
    [
        html.H1("Changing figures with callback_context (CTX)"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([buttons], md=4),
                dbc.Col(dcc.Loading(dcc.Graph(id="Graph"), type="cube"), md=8),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output('Graph', 'figure'),
    [Input('btn-bar', 'n_clicks'),
     Input('btn-line', 'n_clicks'),
     Input('btn-area', 'n_clicks'),
    ]
)
def display(btn_bar, btn_line, btn_area):
    button_id = ctx.triggered_id if ctx.triggered_id else "btn-bar"

    if button_id == "btn-bar":
        return px.bar(data_canada, x="year", y="pop")
    elif button_id == "btn-line":
        return px.line(data_canada, x="year", y="pop")
    else:
        return px.area(data_canada, x="year", y="pop")
    


if __name__ == "__main__":
    app.run_server(debug=True)