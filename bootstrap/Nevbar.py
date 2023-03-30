from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("Entry1"),
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
    className='mb-5',
)


custom_default = dbc.Navbar(
    dbc.Container(
        [
            dbc.Navbar
        ]
    )
)

app.layout = dbc.Container(default)


if __name__ == "__main__":
    app.run_server(debug=True)

