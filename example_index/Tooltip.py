from dash import Dash, html, dcc, Input, Output, no_update
import pandas as pd
import plotly.express as px


df = pd.read_table("https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv")
print(df.shape)
print(df.head())


#cleaning
df['Order Date'] = pd.to_datetime(df["Order Date"])
df["Profit"] = df["Profit"].str.replace(",", ".")
df["Profit"] = df["Profit"].astype("float")


#add columns
df["year_month"] = pd.DatetimeIndex(df['Order Date']).to_period("M").astype("str")


#grouping
df_grouped = (
    df[["Order Date", "Profit"]].groupby(by=pd.Grouper(key="Order Date", axis=0, freq='M')).sum().reset_index()
)


##graph
fig = px.bar(data_frame=df_grouped, x="Order Date", y="Profit", template="simple_white")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.update_traces(hoverinfo="none", hovertemplate=None)


##layout
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Dash Tooltip Example", style={"textAlign": "center"}),        
        dcc.Graph(id="tooltip-graph-basic-2", figure=fig, clear_on_unhover=True),        
        dcc.Tooltip(id="tooltip-graph", direction="left"),        
    ]
)

@app.callback(
    Output("tooltip-graph", "show"),
    Output("tooltip-graph", "bbox"), #좌표
    Output("tooltip-graph", "children"), #그래프 모양
    Input("tooltip-graph-basic-2", "hoverData")
)
def display_hover(hover_data):
    if hover_data is None:
        return False, no_update, no_update
    
    print(hover_data)
    x = hover_data["points"][0]["x"]
    
    date_month = x[:7] #월까지만
    df_filtered = df.query(f"year_month == '{date_month}'")

    df_filtered_grouped = (
        df_filtered[["Segment", "Profit"]].groupby(by="Segment").sum().reset_index()
    )


    ##tooltip
    fig1 = px.bar(
        data_frame=df_filtered_grouped, x="Segment", y="Profit", template="simple_white"
    )
    fig1.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    pt = hover_data["points"][0]
    bbox = pt["bbox"]

    children = [
        html.Div(
            [
                html.H4(f"Year-Month: {date_month}"),
                dcc.Graph(figure=fig1),
            ],
            style={"width": "200px", "height": "200px", "whiteSpace": "normal"},
        )
    ]

    return True, bbox, children



if __name__ == "__main__":
    app.run_server(debug=True)
