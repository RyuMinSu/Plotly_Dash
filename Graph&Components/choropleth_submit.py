import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import plotly.express as px


exterernal_sheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=exterernal_sheets)

app.layout = html.Div([
    html.Div(
        dcc.Graph(id='the_graph')
    ),

    html.Div([
        dcc.Input(
            id='input_state',
            type='number',
            inputMode='numeric',
            value=2007,
            max=2007,
            min=1952,
            step=5,
            required=True
        ),
        html.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit'
        ),
        html.Div(id='output_state'),
    ], style={'text-align': 'center'}),
])


@app.callback(
    [Output('output_state', 'children'),
    Output(component_id='the_graph', component_property='figure')],
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='input_state', component_property='value')]
)
def update_output(num_clicks, val_selected):
    if val_selected is None:
        raise PreventUpdate
    else:
        df = px.data.gapminder().query("year=={}".format(val_selected))

        fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp",
                    hover_name="country",
                    projection='natural earth',
                    title='Life Expectancy by Year',
                    color_continuous_scale=px.colors.sequential.Plasma)

        fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                          margin=dict(l=60, r=60, t=50, b=50))

        return ('The input value was "{}" and the button has been \
                clicked {} times'.format(val_selected, num_clicks), fig)

if __name__ == '__main__':
    app.run_server(debug=True)