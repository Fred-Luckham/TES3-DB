import dash
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

df_cloth = pd.read_csv('csv/Clothing.csv', encoding = 'unicode_escape')

clothing_table = [
    html.Div([
        dash_table.DataTable(
            data=df_cloth.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_cloth.columns],
            fixed_rows={'headers': True, 'data': 0},
            page_size=50,
            style_as_list_view=True,
            style_table={'height': '100%', 'width': '100%', 'overflowX': 'auto'},
            style_cell={
                'height': 'auto',
                'textAlign': 'left',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df_cloth.to_dict('rows')
            ],
            tooltip_duration=None,
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            },
            filter_action="native",
            sort_action="native",
            sort_mode='multi',
        )
    ])
]