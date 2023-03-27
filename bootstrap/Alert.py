"""
구성요소 사용 상황별 피드백 메세지

"""

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    # dbc.Alert("This is a primary alert", color="primary"), #파랑
    # dbc.Alert("This is a secondary alert", color="secondary"), #옅은회색
    # dbc.Alert("This is a success alert! Well done!", color="success"), #초록
    # dbc.Alert("This is a warning alert... be careful...", color="warning"), #노랑
    # dbc.Alert("This is a danger alert. Scary!", color="danger"), #빨강
    # dbc.Alert("This is an info alert. Good to know!", color="info"), #하늘
    # dbc.Alert("This is a light alert", color="light"), #하양
    # dbc.Alert("This is a dark alert", color="dark"), #짙은회색


    ### alert-link로 링크 만들기
    # dbc.Alert([
    #     "This is a primary alert with an ",
    #     html.A("example link", href='https://github.com/RyuMinSu', className='alert-link')
    # ], color='primary'
    # ),

    # dbc.Alert([
    #     "This is a danger alert with an ",
    #     html.A("example link", href="https://github.com/RyuMinSu", className="alert-link"),
    # ], color='warning'
    # )


    ### 컨텐츠 추가
    # dbc.Alert([
    #     html.H4('Well done!', className='alert-heading'),
    #     html.P(
    #         "This is a success alert with loads of extra text in it. So much "
    #         "that you can see how spacing within an alert works with this "
    #         "kind of content."            
    #     ),
    #     html.Hr(),
    #     html.P(
    #         "Let's put some more text down here, but remove the bottom margin",
    #         className="mb-0",
    #     )
    # ])


    ### 사라지기
    dbc.Button(
        "Toggle alert with fade",
        id="alert-toggle-fade",
        className="me-1 mt-2",
        n_clicks=0,),
    dbc.Button(
        "Toggle alert without fade",
         id="alert-toggle-no-fade",
         n_clicks=0),
    html.Hr(),
    dbc.Alert(
        "Hello! I am an alert",
        id="alert-fade",
        dismissable=True, #삭제버튼
        is_open=True,
    ),
    dbc.Alert(
        "Hello! I am an alert that doesn't fade in or out",
        id="alert-no-fade",
        dismissable=True,
        fade=False, #애니메이션 default=True
        is_open=True,
    ),
])

@app.callback(
    Output("alert-fade", 'is_open'),
    [Input('alert-toggle-fade', 'n_clicks')],
    [State("alert-fade", 'is_open')]
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("alert-no-fade", "is_open"),
    [Input("alert-toggle-no-fade", "n_clicks")],
    [State("alert-no-fade", "is_open")],
)
def toggle_alert_no_fade(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)