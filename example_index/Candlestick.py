from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
)
print(df.columns)
print(df.head())

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Apple Stock Candlestick chart"),
        dcc.Checklist(
            id="toggle-rangeslider",
            options=[{"label": "Include RangeSlider", "value": "slider"}],
            value=["slider"],
        ),
        dcc.Graph(id="graph")
    ]
)

@app.callback(
    Output("graph", "figure"),
    Input("toggle-rangeslider", "value")
)
def display_candlestick(value):
    fig = go.Figure(
            go.Candlestick(
                x=df["Date"],
                open=df["AAPL.Open"],
                high=df["AAPL.High"],
                low=df["AAPL.Low"],
                close=df["AAPL.Close"],
            )
    )
    fig.update_layout(
        xaxis_rangeslider_visible="slider" in value
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)