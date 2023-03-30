from dash import Dash, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("this is tab1!", className='card-text'),
            dbc.Button('Click here', color='success'),
        ]
    ),
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab2!", className='card-text'),
            dbc.Button("Don't click here", color="danger", href="https://naver.com"),
        ]
    ),
)

# tabs = html.Div(
#     [ 
#         dbc.Tabs(
#             [
#                 dbc.Tab(label="Tab1", tab_id="tab-1"),
#                 dbc.Tab(label="Tab2", tab_id="tab-2"),
#             ],
#             id="tabs", active_tab="tab-1"
#         ),
#         html.Div(id="content")
#     ]
# )


# card = dbc.Card(
#     [
#         dbc.CardHeader(
#             dbc.Tabs(
#                 [
#                     dbc.Tab(label='Tab 1', tab_id='tab-1'),
#                     dbc.Tab(label="Tab 2", tab_id="tab-2"),
#                 ], id="card-tabs", active_tab="tab-1"
#             )
#         ),
#         dbc.CardBody(
#             html.P(id="card-content", className="card-text")
#         ),
#     ],
# )


# card1 = dbc.Card(
#     [
#         dbc.CardHeader(
#             dbc.Tabs(
#                 [
#                     dbc.Tab(
#                         label='Tab1', tab_id='tab-1', labelClassName="text-success",tabClassName="ms-auto", 
#                     ),
#                     dbc.Tab(
#                         label="Tab2", tab_id="tab-2", labelClassName="text-primary", tabClassName="ms-auto"
#                     ),
#                 ], id="card-tabs", active_tab='tab-1'
#             ),
#         ),
#         dbc.CardBody(
#             html.P(id="card-content", className="card-text")
#         ),
#     ]
# )


tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Tab1", tab_id="tab-1", tabClassName='ms-auto', activeLabelClassName="text-success", activeTabClassName="fw-bold fst-italic"),
                dbc.Tab(label="Tab2", tab_id="tab-2", activeLabelClassName="text-success", activeTabClassName="fw-bold fst-italic"),
            ], id="tabs", active_tab='tab-1'
        ), html.Div(id="content")
    ]
)



app.layout = dbc.Container(tabs)

@app.callback(
    Output('content', 'children'),
    [Input('tabs', 'active_tab')]
)
def switch_tab(active_tab):
    if active_tab == "tab-1":
        return tab1_content
    elif active_tab == "tab-2":
        return tab2_content
    return "Disabled"


if __name__ == "__main__":
    app.run_server(debug=True)