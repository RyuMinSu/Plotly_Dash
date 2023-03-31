import dash_bootstrap_components as dbc
from dash import Dash, html
from dash.dependencies import Input, Output, State


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

offcanvas = html.Div(
    [
        dbc.Button("Open offcanvas", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            html.P(
                "This is the content of the Offcanvas. "
                "Close it by clicking on the close button, or "
                "the backdrop."                
            ), id = 'offcanvas', title="Title", is_open=False
        )
    ]
)

app.layout = dbc.Container(offcanvas)


@app.callback(
    Output('offcanvas', 'is_open'),
    [Input('open-offcanvas', 'n_clicks')],
    [State('offcanvas', 'is_open')]

)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)