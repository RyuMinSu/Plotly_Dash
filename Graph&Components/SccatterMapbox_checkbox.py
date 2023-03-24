import pandas as pd

import dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

import plotly.offline as py
import plotly.graph_objects as go


mapbox_access_token = open(r"Plotly_Dash\mapbox_token.txt").read()
# print(mapbox_access_token)

blackbold = {'color':'black', 'font-weight': 'bold'}


# data -----------------------------------------------------------------------

df = pd.read_csv(r"Plotly_Dash\data\finalrecycling.csv")
print(df.shape)
print(df.columns)
print(df.head())

# layout --------------------------------------------------------------------

css2_path= r"Plotly_Dash\Graph&Components\assets\venues_styling.css"
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', css2_path]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            # Map legend
            html.Ul([
                html.Li("Compost", className='circle', style={'background': '#ff00ff','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Electronics", className='circle', style={'background': '#0000ff','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Hazardous_waste", className='circle', style={'background': '#FF0000','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Plastic_bags", className='circle', style={'background': '#00ff00','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Recycling_bins", className='circle', style={'background': '#824100','color':'black',
                    'list-style':'none','text-indent': '17px'}),
            ], style={'border-bottom': 'solid 3px', 'border-color':'#00FC87','padding-top': '6px'}),

            # Borough_checklist
            html.Label(['Borough: '], style=blackbold),
            dcc.Checklist(
                id='boro_name',
                options=[{'label':str(b), 'value':b} for b in sorted(df['boro'].unique())],
                value=[b for b in sorted(df['boro'].unique())],
            ),

            # Recycling type checklist
            html.Label(['Looking to recycle: '], style=blackbold),
            dcc.Checklist(
                id='recycling_type',
                options=[{'label':str(b), 'value':b} for b in sorted(df['type'].unique())],
                value=[b for b in sorted(df['type'].unique())]
            ),

            #web link
            html.Br(),
            html.Label(['Website:'], style=blackbold),
            html.Pre(
                id='web_link', children=[],
                style={'white-space': 'pre-wrap','word-break': 'break-all',
                    'border': '1px solid black','text-align': 'center',
                    'padding': '2rem', 'color':'blue',
                    'margin-top': '1rem'}
            )
        ], className='three columns'
        ),

        #Map
        html.Div(
            dcc.Graph(id='graph'),
            className='nine columns',
        ),
    ], className='row'
    )
], className='ten columns offset-by-one'
)


# callback ------------------------------------------------------------------

#Map
@app.callback(
    Output('graph', 'figure'),
    [Input('boro_name', 'value'),
     Input('recycling_type', 'value')]
)
def update_figure(chosen_boro, chosen_recycling):
    cond1 = df['boro'].isin(chosen_boro)
    cond2 = df['type'].isin(chosen_recycling)

    df_sub = df[(cond1)&(cond2)]

    locations = [
        go.Scattermapbox(
            lon = df_sub['longitude'],
            lat = df_sub['latitude'],
            mode = 'markers',
            marker = {'color': df_sub['color']},
            unselected={'marker' : {'opacity':1}}, #선택 x
            selected={'marker' : {'opacity':0.5, 'size':25}}, #선택 o
            hoverinfo='text',
            hovertext=df_sub['hov_txt'], #마우스 올렸을때
            customdata=df_sub['website'], #선택시 포함할 데이터
        )
    ]

    return {
        'data': locations,
        'layout': go.Layout(
            uirevision= 'foo',
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            title={
                "text": "Where to Recycle My Stuff",
                "font": {'size':50, 'color':'green'}
            },
            mapbox={
                'accesstoken': mapbox_access_token,
                'bearing':25,
                'style':'light',
                'center': {
                    'lat':40.80105,
                    'lon':-73.945155
                },
                'pitch':40,
                'zoom':11.5
            }
        )        
    }

#Web link
@app.callback(
    Output('web_link', 'children'),
    Input('graph', 'clickData')
)
def display_click_data(clickData):
    if clickData is None:
        return 'Click on any bubble'
    else:
        print (clickData)
        the_link=clickData['points'][0]['customdata']
        if the_link is None:
            return 'No Website Available'
        else:
            return html.A(the_link, href=the_link, target="_blank")
    


if __name__ == "__main__":
    app.run_server(debug=True)