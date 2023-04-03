from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = px.data.election()
print(df.shape)
print(df.columns)
print(df.head())

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Political candidate voting pool analysis"),
        html.P("Select a candidate:"),
        dcc.RadioItems(
            id="candidate",
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True
        ),
        dcc.Graph(id="graph"),
    ]
)

@app.callback(
    Output("graph", "figure"),
    Input("candidate", "value"),
)
def display_choropleth(candidate):
    geojson = px.data.election_geojson()
    # print(geojson)

    fig = px.choropleth(
        data_frame=df,
        geojson=geojson,
        color=candidate,
        locations="district",
        featureidkey="properties.district",
        projection="mercator",
        range_color=[0, 6500],
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"t":0, "r":0, "b":0, "l":0})
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)