import pandas as pd

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv(r"Plotly_Dash\data\DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
# print(df.shape)
# print(df.columns)

# data cleaning -----------------------------------------------------------
"""
1. INSPECTION DATE: 날짜로 변경
2. 'INSPECTION DATE','CUISINE DESCRIPTION','CAMIS'로 그룹화 하여 스코어 평균
3. INSPECTION_DATE 인덱스로 설정
4. 2016.01.01 ~ 2019.12.31 데이터 사용
5. 월별 집계
"""

##1
df['INSPECTION DATE'] = pd.to_datetime(df['INSPECTION DATE'])

##2: as_index=False!!
df = df.groupby(['INSPECTION DATE','CUISINE DESCRIPTION','CAMIS'], as_index=False)['SCORE'].mean()

##3
df = df.set_index('INSPECTION DATE')

##4
df = df.loc['2016-01-01': '2019-12-31']

##5
df = df.groupby([pd.Grouper(freq='M'),'CUISINE DESCRIPTION'])['SCORE'].mean().reset_index()
# print(df.head(10))


# layout --------------------------------------------------------------------



app.layout = html.Div([
    html.Div(
        dcc.Graph(id='our_graph'),
        className='nine columns'
    ), 
    
    #cuisine
    html.Div([
        html.Br(),
        html.Label(
            ['Choose 3 Cuisines to Compare:'],
            style={'font-weight': 'bold', 'text-align': 'center'}),
        dcc.Dropdown(
            id = 'cuisine_one',
            options=[{'label':x, 'value':x} for x in df.sort_values('CUISINE DESCRIPTION')['CUISINE DESCRIPTION'].unique()],
            value = 'African',
            multi=False,
            disabled=False,
            clearable=True,
            placeholder='Choose Cuisine...', #value없을때
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory',
        ),
        #cuisine2
        dcc.Dropdown(
            id='cuisine_two',
            options=[{'label':x, 'value':x} for x in df.sort_values('CUISINE DESCRIPTION')['CUISINE DESCRIPTION'].unique()],
            value='Asian',
            multi=False,
            clearable=False,
            searchable=True,
            persistence='string',
            persistence_type='session'
        ),
        #cuisine3
        dcc.Dropdown(
            id='cuisine_three',
            options=[{'label':x, 'value':x} for x in df.sort_values('CUISINE DESCRIPTION')['CUISINE DESCRIPTION'].unique()],
            value='Donuts',
            multi=False,
            clearable=False,
            persistence='string',
            persistence_type='local'),
    ], className='three columns'),
])


# callback ------------------------------------------------------------------

@app.callback(
    Output('our_graph', 'figure'),
    [Input('cuisine_one','value'),
     Input('cuisine_two','value'),
     Input('cuisine_three','value')]
)
def build_graph(first_cuisine, second_cuisine, third_cuisine):
    cond1 = df['CUISINE DESCRIPTION'] == first_cuisine
    cond2 = df['CUISINE DESCRIPTION'] == second_cuisine
    cond3 = df['CUISINE DESCRIPTION'] == third_cuisine

    dff = df[(cond1)|(cond2)|(cond3)] 

    fig = px.line(
        data_frame=dff,
        x="INSPECTION DATE",
        y="SCORE",
        color='CUISINE DESCRIPTION',
        height=600
    )
    fig.update_layout(
        yaxis={'title': 'NAVIGATE POINT'},
        title={'text': 'Restaurant Inspections in NYC'},
        font={'size':28}
    )
    fig.update_annotations(
        x=.5, xanchor='center'
    )

    return fig




if __name__ == '__main__':
    app.run_server(debug=True)
