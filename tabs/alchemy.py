import dash
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

df = pd.read_csv('csv/Alchemy.csv', encoding = 'unicode_escape')

alchemy_table = [
    html.Div([
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            fixed_rows={'headers': True, 'data': 0},
            style_as_list_view=True,
            style_table={'overflowX': 'auto'},
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
                } for row in df.to_dict('rows')
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
            }
        )
    ])
]