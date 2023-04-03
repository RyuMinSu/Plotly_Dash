from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Interactive figure controls with Dash"),
        html.P("Font size:"),
        dcc.Slider(
            id="font_size", min=10, max=35, value=25
        ),
        html.P("Title Text"),
        dcc.Input(
            id="input-text",
            style={"width": "100%"},
            value="Change the title",
        ),
        dcc.Graph(id="graph"),
    ]
)

@app.callback(
    Output("graph", "figure"),
    [Input("input-text", "value"),
     Input("font_size", "value"),]
)
def update_chart(text, font_size):
    fig = px.bar(x=[1, 2, 3], y=[1, 3, 2])
    fig = go.Figure(fig)
    fig.update_layout(title_text=text, title_font_size=font_size)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)