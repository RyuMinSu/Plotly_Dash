from dash import Dash, html, dcc, Input, Output
import plotly.express as px


df = px.data.gapminder()
# print(df.shape)
# print(df.head())

# object_cols = ["country", "continent", "iso_alpha", "iso_num"]
# num_cols = [col for col in df.columns if not col in object_cols ]
# print(object_cols)
# print(num_cols)


# for col in object_cols:    
#     print(f"\nobjcols_{col}", "-"*20)
#     print(df[col].value_counts(dropna=False))


# for col in num_cols:    
#     print(f"\nnum_cols_{col}", "-"*20)
#     print(df[col].value_counts(dropna=False))



app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Animation GDP and population over decades"),
        html.P("Select an animation"),
        dcc.RadioItems(
            id="selection",
            options=["GDP - Scatter", "Population - Bar"],
            value="GDP - Scatter",
        ),
        dcc.Loading(dcc.Graph(id='graph'), type='cube')
    ]
)


@app.callback(
    Output('graph', 'figure'),
    [Input('selection', 'value')]
)
def display_animated_graph(selection):
    animations = {        
        "GDP - Scatter": px.scatter(
            df,
            x="gdpPercap",
            y="lifeExp",
            color="continent",
            size="pop",
            size_max=55,
            log_x=True,
            hover_name="country",
            range_x=[100, 100000],
            range_y=[25, 90],
            animation_frame="year",
            animation_group="country",
        ),
        "Population - Bar": px.bar(
            df,
            x='continent',
            y="pop",
            color="continent",
            animation_frame="year",
            animation_group="country",
            range_y=[0, 4000000000],
        )
    }
    return animations[selection]


if __name__ == "__main__":
    app.run_server(debug=True)