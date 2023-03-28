"""
버튼 & 뱃지

"""

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div(
#     dbc.Button([
#         'Notification',
#         dbc.Badge("4", color='light', text_color='primary', className='ms-2')
#     ])
# )



# badge = dbc.Button(
#     ["Notifications",
#      dbc.Badge("4", color="light", text_color="primary", className="ms-1"),
#     ],
#     color="primary",
# )

# app.layout = dbc.Container(badge, fluid=True)



# badges = html.Div(
#     [
#         html.H1(['Example heading', dbc.Badge('New', className='ms-1')]),
#         html.H2(['Example heading', dbc.Badge('New', className='ms-1')]),
#         html.H3(['Example heading', dbc.Badge('New', className='ms-1')]),
#         html.H4(['Example heading', dbc.Badge('New', className='ms-1')]),
#         html.H5(['Example heading', dbc.Badge('New', className='ms-1')]),
#         html.H6(['Example heading', dbc.Badge('New', className='ms-1')]),
#     ]
# )


# badges = html.Span(
#     [
#         dbc.Badge("Primary", color="primary", className='me-1'),
#         dbc.Badge("Secondary", color="secondary", className="me-1"),
#         dbc.Badge("Success", color="success", className="me-1"),
#         dbc.Badge("Warning", color="warning", className="me-1"),
#         dbc.Badge("Danger", color="danger", className="me-1"),
#         dbc.Badge("Info", color="info", className="me-1"),
#         dbc.Badge("Light", text_color="dark", color="light", className="me-1"),
#         dbc.Badge("Dark", color="dark"),
#     ]
# )


# badges = html.Span(
#     [
#         dbc.Badge(
#             "primary",
#             color='white',
#             text_color='primary',
#             className='border me-1',
#             pill=True
#         ),
#         dbc.Badge(
#             "Secondary",
#             color="white",
#             text_color="secondary",
#             className="border me-1",
#             pill=True
#         ),
#         dbc.Badge(
#             "Success",
#             color="white",
#             text_color="success",
#             className="border me-1",
#             pill=True
#         ),
#         dbc.Badge(
#             "Warning",
#             color="white",
#             text_color="warning",
#             className="border me-1",
#             pill=True
#         ),
#         dbc.Badge(
#             "Danger",
#             color="white",
#             text_color="danger",
#             className="border me-1",
#         ),
#         dbc.Badge(
#             "Info", color="white", text_color="info", className="border me-1", pill=True
#         ),
#         dbc.Badge(
#             "Dark", color="white", text_color="dark", className="border me-1"
#         ),
#         dbc.Badge(
#             "Black",
#             color="white",
#             text_color="black",
#             className="border me-1",
#         ),
#         dbc.Badge(
#             "Muted",
#             color="white",
#             text_color="muted",
#             className="border me-1",
#         ),
#         dbc.Badge(
#             "Light",
#             color="secondary",
#             text_color="light",
#             className="border me-1",
#             pill=True
#         ),
#         dbc.Badge(
#             "White", color="secondary", text_color="white", className="border"
#         ),
#     ]
# )

badge = dbc.Button(
    [
        "Notification",
        dbc.Badge(
            "99+",
            color="danger",
            pill=True,
            text_color='white',
            className='position-absolute',
            href="https://github.com/RyuMinSu",
        )
    ]
)


app.layout = dbc.Container(badge, fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)