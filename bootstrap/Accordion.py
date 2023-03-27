"""
접을 수 있는 목록 사용
목록 하나 클릭하면 하나가 접힘-제일처음꺼 열려있음 (default)
시작시 아무것도 안열리게: start_collapsed=True
주위 테두리 없애기: flush=True
항상 안닫히게: always_open=True
아이템 하나당 id지정하여 콜백으로 어떤것이 열렸는지 나타낼 수 있음

"""

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Accordion([
        dbc.AccordionItem([
            # 펼쳤을때 내용
            html.P("This is the content of the first section"),
            # 펼쳤을때 버튼
            dbc.Button('Click here'),            
        ], title='Item1', item_id='item-1'
        ),

        dbc.AccordionItem([
            # 펼쳤을때 내용
            html.P("This is the content of the second section"),
            # 펼쳤을때 버튼
            dbc.Button('Click here'),
        ], title='Item2', item_id='item-2'
        ),

        dbc.AccordionItem([
            # 펼쳤을때 내용
            html.P("This is the content of the third section"),
            # 펼쳤을때 버튼
            dbc.Button('Click here'),            
        ], title='Item3', item_id='item-3'
        ),        
    ],
    start_collapsed=True, # 시작시 아무것도 안열리게
    flush=True, # 주위 테두리 없애기    
    always_open=True, # 다른거 열릴때 열려있는거 안닫히게 하기
    id='accordion', active_item='' #active_item지정 해야 콜백시 나타남
    ),
    
    html.Div(id='accordian-contents', className='mt-3'),
])



@app.callback(
    Output('accordian-contents', 'children'),
    [Input('accordion', 'active_item')]
)
def change_item(item):
    return f"Item selected: {item}"

if __name__ == "__main__":
    app.run_server(debug=True)