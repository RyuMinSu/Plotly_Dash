import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# card = dbc.Card(
#     [
#         dbc.CardImg(src=r"Plotly_Dash\image\docker.png", top=True),
#         dbc.CardBody(
#             [
#                 html.H4("CardTitle", className='card-title'),
#                 html.P(
#                     "Some quick example text to build on the card title and "
#                     "make up the bulk of the card's content.",
#                 ),
#                 dbc.Button('Go somewhere', color='primary'),
#             ]
#         )
#     ], 
#     style={'width':'18rem'}
# )

# card = dbc.Card(
#     [
#         dbc.CardImg(src=r"Plotly_Dash\image\docker.png", top=True),
#         dbc.Card(
#             [
#                 html.H4("CardTitle", className='card-title'),
#                 html.P(
#                     "Some quick example text to build on the card title and "
#                     "make up the bulk of the card's content.",
#                 ),
#                 dbc.Button('Go somewhere', color='primary'),
#             ], body=True
#         )
#     ], 
#     style={'width':'18rem'}
# )


# card = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H4("Title", className="card-title"),
#             html.H6("Card subtitle", className="card-subtitle"),
#             html.P(
#                 "Some quick example text to build on the card title and make "
#                 "up the bulk of the card's content.",
#                 className="card-text",
#             ),
#             dbc.CardLink("Card link", href="#"),
#             dbc.CardLink("External link", href="https://google.com"),
#         ]
#     )
# )



# top_card = dbc.Card(
#     [
#         dbc.CardImg(src=r"Plotly_Dash\image\docker.png", top=True),
#         dbc.CardBody(
#             html.P("This card has an image at the top", className='card-text')
#         )
#     ], style={"width":"18rem"}
# )

# bottom_card = dbc.Card(
#     [
#         dbc.CardBody(html.P("This has a bottom image", className="card-text")),
#         dbc.CardImg(src="/static/images/placeholder286x180.png", bottom=True),
#     ], style={"width":"18rem"}
# )

# cards = dbc.Row(
#     [
#         dbc.Col(top_card, width='auto'),
#         dbc.Col(bottom_card, width='auto')
#     ]
# )



# card = dbc.Card(
#     [
#         dbc.CardImg(src=r"Plotly_Dash\image\docker.png", top=True, style={'opcacity':0.3}),
#         dbc.CardImgOverlay(
#             dbc.CardBody(
#                 [
#                     html.H4("Card Title", className='card-title'),
#                     html.P(
#                         "An example of using an image in the background of "
#                         "a card.",
#                         className="card-text",
#                     ),
#                     dbc.Button("Go somewhere", color="primary"),
#                 ],
#             ),
#         ),        
#     ],
# )

# card = dbc.Card(
#     dbc.ListGroup(
#         [
#             dbc.ListGroupItem("Item 1"),
#             dbc.ListGroupItem("Item 2"),
#             dbc.ListGroupItem("Item 3"),
#         ],
#         flush=True,
#     ),
#     style={"width": "18rem"},
# )



# card = dbc.Card(
#     [
#         dbc.CardHeader("This is the header"),
#         dbc.CardBody(
#             [
#                 html.H4("card title", className='card-title'),
#                 html.P('This is some card text', className='card-text'),
#             ]
#         )
#     ]
# )



# first_card = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H5("Card title", className='card-title'),
#             html.P('This card has some text content'),
#             dbc.Button("Go somewhere", color='primary'),
#         ],
#     ),
# )

# second_card = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H5("Cardtitle", className='card-title'),
#             html.P(
#                 "This card also has some text content and not much else, but "
#                 "it is twice as wide as the first card."                
#             ),
#             dbc.Button('Go somewhere', color='primary'),
#         ],
#     ),
# )


# cards = dbc.Row(
#     [
#         dbc.Col(first_card, width=4),
#         dbc.Col(second_card, width=8),
#     ]
# )


# cards = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H5('custom css', className='card-title'),
#             html.P(
#                 "This card has inline styles applied controlling the width. "
#                 "You could also apply the same styles with a custom CSS class."
#             ),
#         ],
#     ),
#     style={'width':'18rem'},
# )



# card_content = [
#     dbc.CardHeader('Card header', className='card-title'),
#     dbc.CardBody(
#         [
#             html.H5('Card title', className='card-title'),
#             html.P(
#                 'This is some card conetent that ......',
#                 className='card-text'
#             ),
#         ],
#     ),
# ]

# cards = html.Div(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(dbc.Card(card_content, color='primary', inverse=True)),
#                 dbc.Col(dbc.Card(card_content, color='warning', outline=True, )),
#                 dbc.Col(dbc.Card(card_content, color='danger')),
#             ],
#             className='mb-4'
#         ),
#         dbc.Row(
#             [
#             dbc.Col(dbc.Card(card_content)),
#             dbc.Col(dbc.Card(card_content)),
#             dbc.Col(dbc.Card(card_content)),
#             ],
#             className='mb-4'
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(dbc.Card(card_content)),
#                 dbc.Col(dbc.Card(card_content)),
#             ],
#             className='mb-4'
#         )
#     ]
# )



###카드그룹
cards = dbc.CardGroup(
    [
        dbc.Card(
            [
                html.H5('card1', className='card-title'),
                html.P(
                    "This card has some text content, which is a little "
                    "bit longer than the second card.",
                    className="card-text",
                ),
                dbc.Button(
                    "Click here", color="success", className="mt-auto"
                ),
            ],
            style={'padding':'2rem'}
        ),
        dbc.Card(
            [
                html.H5('card2', className='card-title'),
                html.P(
                    "This card has some text content.",
                    className="card-text",
                ),
                dbc.Button(
                    "Click here", color="warning", className="mt-auto"
                ),
            ]
        ),
        dbc.Card(
            [
                html.H5('card3', className='card-title'),
                html.P(
                    "This card has some text content, which is longer "
                    "than both of the other two cards, in order to "
                    "demonstrate the equal height property of cards in a "
                    "card group.",
                    className="card-text",
                ),
                dbc.Button(
                    "Click here", color="danger", className="mt-auto"
                ),
            ]
        ),
    ],
)



app.layout = dbc.Container(cards, fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)