from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

filepath = (
    "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
)

df = pd.read_csv(filepath)

# print(df.shape)
# print(df.columns)
# print(df.info())

state_list = df["state"].unique()
print(state_list)


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("Polar Charts of U.S. Agricultural Exports, 2011", style={"text-align": "center"}),
        html.Div("Choose the radius scale:"),
        dcc.RadioItems(
            id="bar-polar-app-x-radio-items",
            options=["Absolute", "Logarithmic"],
            value="Logarithmic",
        ),
        
        html.Br(),
        dcc.Dropdown(
            id="bar-polar-app-x-dropdown",
            options=state_list,
            value=state_list[:6],
            multi=True,
        ),

        dcc.Loading(dcc.Graph(id="bar-polar-app-x-graph"), type="cube")
    ]
)

@app.callback(
    Output('bar-polar-app-x-graph', 'figure'),
    [Input('bar-polar-app-x-dropdown', 'value'),
     Input('bar-polar-app-x-radio-items', 'value'),]
)
def update_graph(state, radius_scale):
    dff = df[df['state'].isin(state)]
    log_r = True if radius_scale == "Logarithmic" else False

    fig = px.bar_polar(
        dff,
        r = dff["total exports"],
        theta = dff["state"],
        color = dff["total exports"], #bar color
        template = 'plotly_white', 
        color_continuous_scale=px.colors.sequential.Plasma,
        log_r=log_r
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)