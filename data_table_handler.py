import dash
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

def data_table(csv_file):
    # read csv file
    path = "csv/{0}.csv".format(csv_file)
    df = pd.read_csv(path, encoding = 'ISO-8859-1')

    table = dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df.columns],
                page_size=15,
                fixed_rows={
                    'headers': True},
                style_table={
                    'height': '100%',
                    'overflowY': 'auto',
                    'border-radius': '15px',
                    'border': '4px solid #A9A9A9'
                },
                style_cell={
                    'height': 'auto',
                    'textAlign': 'left',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                    'whiteSpace': 'normal'
                },
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

    return table