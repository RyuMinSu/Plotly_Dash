import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import plotly.express as px


df = pd.read_csv(r"Plotly_Dash\data\suicide_rates.csv")
print(df.shape)
print(df.columns)

mark_values = {1985:'1985',1988:'1988',1991:'1991',1994:'1994',
               1997:'1997',2000:'2000',2003:'2003',2006:'2006',
               2009:'2009',2012:'2012',2015:'2015',2016:'2016'}

app = dash.Dash(__name__)


# layout -----------------------------------------------------------------------------
app.layout = html.Div([
    html.Div(
        html.Pre(children='Suicide Rates 1985-2016'),
        style={"text-align": "center", "font-size":"100%", "color": "black"}
    ), #제목

    html.Div(
        dcc.Graph(id='the_graph')
    ), #그래프

    html.Div(
        dcc.RangeSlider(
            id='the_year',
            min=1985,
            max=2016,
            value=[1985, 1988],
            marks=mark_values,
            step=None,
        ), style={"width": "70%", "position":"absolute",
                 "left":"5%"}
    ), #슬라이더
])

#callback ------------------------------------------------------------------------------
@app.callback(
    Output('the_graph', 'figure'),
    Input('the_year', 'value'),
)

def update_graph(year_chosen):
    #year_chosen은 2개의 값이 들어올 것임
    dff = df[(df['year'] >= year_chosen[0]) & (df['year'] <= year_chosen[1])]
    dff = dff.groupby(['country'], as_index=False)[["suicides/100k pop", "gdp_per_capita ($)"]].mean()
    # print(dff[:3])

    scatterplot = px.scatter(
        data_frame=dff,
        x='suicides/100k pop',
        y="gdp_per_capita ($)",        
        text='country',
        height=550,
    )

    scatterplot.update_traces(textposition='top center')

    return (scatterplot)

if __name__ == "__main__":
    app.run_server(debug=True)
