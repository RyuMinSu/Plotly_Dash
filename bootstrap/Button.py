import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# buttons = html.Div(
#     [
#         dbc.Button("Primary", color="primary", className="me-1"),
#         dbc.Button("Secondary", color="secondary", className="me-1"),
#         dbc.Button("Success", color="success", className="me-1"),
#         dbc.Button("Warning", color="warning", className="me-1"),
#         dbc.Button("Danger", color="danger", className="me-1"),
#         dbc.Button("Info", color="info", className="me-1"),
#         dbc.Button("Light", color="light", className="me-1"),
#         dbc.Button("Dark", color="dark", className="me-1"),
#         dbc.Button("Link", color="link"),
#     ]
# )


# button = html.Div(
#     [
#         dbc.Button(
#             'Click Me', id="example-button", n_clicks=0, className='me-2', outline=False, color='danger',
#         ),
#         html.Span(id='example-output',)
#     ]
# )

# @app.callback(
#     Output('example-output', 'children'),
#     [Input('example-button', 'n_clicks')]
# )
# def on_button_click(n):
#     if n is None:
#         return "Not clicked"
#     else:
#         return f"clicked {n} times"


# buttons = html.Div(
#     [
#         dbc.Button("Large button", size='lg', className='me-1'),
#         dbc.Button("regular button", className='me-1'),
#         dbc.Button("small button", size='sm'),
#     ],
#     className='d-grid gap-2 col-6 mx-auto'
# )


# buttons = html.Div(
#     [
#         dbc.Button("Large button", size='lg', className='me-1'),
#         dbc.Button("regular button", className='me-1'),
#         dbc.Button("small button", size='sm'),
#     ],
#     className='d-grid gap-2 col-6 d-md-block'
# )


# buttons = html.Div(
#     [
#         dbc.Button('Regular', color='primary', className='me-1'),
#         dbc.Button('Active', color='primary', active=True, className='me-1'),
#         dbc.Button('disable', color='primary', disabled=True)
#     ]
# )


##button group
button_group = dbc.ButtonGroup(
    [
        dbc.Button("First", color='primary'),
        dbc.Button("Second", color='danger'),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("item1"),
                dbc.DropdownMenuItem('item2'),
            ],
            label='Dropdown', group=True
        )
    ], vertical=True
)


app.layout = dbc.Container(button_group, fluid=True)






if __name__ == "__main__":
    app.run_server(debug=True)
