import os
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from data_table_handler import data_table


app = dash.Dash(__name__)

server = app.server


app.layout = html.Div([
                html.P(
                    "TES3 Game Data Database",
                    style = {
                        'border-radius': '25px',
                        'border': '2px solid #A9A9A9',
                        'font-family': 'monospace',
                        'text_align': 'center',
                        'padding': '10px'
                        }
                    ),
                    dcc.Dropdown(
                                id='dropdown',
                                options=[
                                        {'label': 'Activator', 'value': '1'},
                                        {'label': 'Alchemy', 'value': '2'},
                                        {'label': 'Apparatus', 'value': '3'},
                                        {'label': 'Armor', 'value': '4'},
                                        {'label': 'Book', 'value': '5'},
                                        {'label': 'Class', 'value': '6'},
                                        {'label': 'Clothing', 'value': '7'},
                                        {'label': 'Container', 'value': '8'},
                                        {'label': 'Enchanting', 'value': '9'},
                                        {'label': 'Ingredients', 'value': '10'},
                                        {'label': 'Leveled Creatures', 'value': '11'},
                                        {'label': 'Leveled Items', 'value': '12'},
                                        {'label': 'Light', 'value': '13'},
                                        {'label': 'Lockpick', 'value': '14'},
                                        {'label': 'Misc', 'value': '15'},
                                        {'label': 'NPC', 'value': '16'},
                                        {'label': 'Probe', 'value': '17'},
                                        {'label': 'Race', 'value': '18'},
                                        {'label': 'Repair', 'value': '19'},
                                        {'label': 'Sound Gen', 'value': '20'},
                                        {'label': 'Sound', 'value': '21'},
                                        {'label': 'Spell', 'value': '22'},
                                        {'label': 'Static', 'value': '23'},
                                        {'label': 'Weapon', 'value': '24'},

                                        ],
                                style={
                                    'font-family': 'monospace',
                                },
                                searchable=False),
                    html.Div(
                        id='dropdown-content',
                        style={
                            'height': '100%',
                            'width': '100%'
                        }
                        )
])

@app.callback(
    Output('dropdown-content', 'children'),
    [Input('dropdown', 'value')])
def update_ouput(value):
    if value == '1':
        return data_table('Activator')
    elif value == '2':
        return data_table('Alchemy')
    elif value == '3':
        return data_table('Apparatus')
    elif value == '4':
        return data_table('Armor')
    elif value == '5':
        return data_table('Book')
    elif value == '6':
        return data_table('Class')
    elif value == '7':
        return data_table('Clothing')
    elif value == '8':
        return data_table('Container')
    elif value == '9':
        return data_table('Enchanting')
    elif value == '10':
        return data_table('Ingredient')
    elif value == '11':
        return data_table('Leveled Creature')
    elif value == '12':
        return data_table('Leveled Item')
    elif value == '13':
        return data_table('Light')
    elif value == '14':
        return data_table('Lockpick')
    elif value == '15':
        return data_table('Misc')
    elif value == '16':
        return data_table('NPC')
    elif value == '17':
        return data_table('Probe')
    elif value == '18':
        return data_table('Race')
    elif value == '19':
        return data_table('Repair')
    elif value == '20':
        return data_table('Sound Gen')
    elif value == '21':
        return data_table('Sound')
    elif value == '22':
        return data_table('Spell')  
    elif value == '23':
        return data_table('Static')
    elif value == '24':
        return data_table('Weapon')

if __name__ == '__main__':
    app.run_server(debug=True)