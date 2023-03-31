from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("Entry1", href='https://github.com/'),
        dbc.DropdownMenuItem("Entry2"),        
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu"
)

default = dbc.NavbarSimple(
    children=[nav_item, dropdown],
    brand="default",
    brand_href="#",
    sticky="top",
    className='mb-3',
)


custom_default = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("custom default", href='#'),
            dbc.NavbarToggler(id="navbar-toggler1"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, dropdown], className="ms-auto", navbar=True
                ),
                id="navbar-collapse1",
                navbar=True,
            ),
        ]
    ),
    className="mb-3",
)


logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Logo", className="ms-2")),
                    ], align='center', className="g-0",
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, dropdown],
                    className="ms-auto", navbar=True
                ), id="navbar-collapse2", navbar=True,
            )
        ],
    ), color="dark", dark=True, className='mb-3'
)


search_navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Search", href="#"),
            dbc.NavbarToggler(id="navbar-toggler3"),
            dbc.Collapse(                
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Input(type='search', placeholder='Search')
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Search", color="primary", className="m-2"
                            ), width='auto'
                        ),
                    ], className="ms-auto g-0 flex-nowrap mt-3 mt-md-0", align='center'
                ), navbar=True, id="navbar-collapse3"
            ),
        ]
    ), className='mb-3', color="dark", dark=True,
)



dashboard = dbc.Navbar(
    dbc.Container(
        [
            dbc.Col(
                dbc.NavbarBrand('Dashboard', href="#"), sm=3, md=2
            ),
            dbc.Col(
                dbc.Input(type='search', placeholder="Search hear"),
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(
                        dbc.NavItem(dbc.NavLink("Sign out"))
                    ), navbar=True
                ), width="auto"
            ),
        ]
    ), color='dark', dark=True
)

app.layout = dbc.Container([default, custom_default, logo, search_navbar, dashboard])


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [1, 2, 3]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")]
    )(toggle_navbar_collapse)


if __name__ == "__main__":
    app.run_server(debug=True)

