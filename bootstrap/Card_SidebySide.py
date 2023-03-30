from dash import Dash, html
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])

plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"


card_sales = dbc.Card(
    dbc.CardBody(
        [   
            dbc.CardLink(
                [
                    html.Img(src=plotly_logo_dark, height="50px", className="me-2"),
                    html.Span("Sales")
                ], className='text-decoration-none h2', href="https://plotly.com/careers/"
            ),            
            html.H3("$106.7M"),
            html.Div([html.I("5.8%", className="bi bi-caret-up-fill text-success"), "vs LY"]),
        ], className="border-start border-success border-5"
    ), className="text-center m-4 shadow"
)

card_profits = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-bank me-2"), "Profit"], className="text-nowrap"),
            html.H3("$8.3M"),
            html.Div([html.I("12.3%", className="bi bi-caret-down-fill text-danger"), "vs LY"]),
        ], className="border-start border-danger border-5"
    ), className="text-center m-4 shadow"
)

card_orders = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-cart me-2"), "Orders"], className="text-nowrap"),
            html.H3("91.4K"),
            html.Div([html.I("10.3%", className="bi bi-caret-up-fill text-success"), "vs LY"]),
        ], className='border-start border-success border-5'
    ), className="text-center m-4 shadow"
)

cards = dbc.Row(
    [dbc.Col(card_sales), dbc.Col(card_profits), dbc.Col(card_orders)]
)




# icons1 = ["bi bi-currency-dollar me-2", "bi bi-bank me-2", "bi bi-cart me-2"]
# icons2 = ["bi bi-caret-up-fill", "bi bi-caret-down-fill", "bi bi-caret-up-fill"]
# summary1 = ["Sales", "Profits", "Orders"]
# summary2 = ["5.8%", "12.3%", "10.3%"]
# dollars = ["$106.7M", "%8.3M", "91.4K"]

# def make_card(sm1, ic1, sm2, ic2, dl):
#     return dbc.Card(
#                 dbc.CardBody(
#                     [
#                         html.H1([html.I(className=ic1), sm1], className="text-nowrap"),
#                         html.H3(dl),
#                         html.Div([html.I(summary2, className=ic2), "vs LY"]),
#                     ], className='border-start border-success border-5'
#                 ), className="text-center m-4 shadow"
#             )

# cards = dbc.Row(
#     [dbc.Col(make_card(a, b, c, d, e)) for a, b, c, d, e in zip(summary1, icons1, summary2, icons2, dollars)]
# )

app.layout = dbc.Container(cards)

if __name__ == "__main__":
    app.run_server(debug=True)

