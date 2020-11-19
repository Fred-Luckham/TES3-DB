import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

import tabs.activators
import tabs.alchemy
import tabs.apparatus
import tabs.armor
import tabs.book
import tabs.classes
import tabs.clothing
import tabs.container
import tabs.enchanting
import tabs.ingredients
import tabs.leveled_creature
import tabs.leveled_item
import tabs.light
import tabs.lockpick
import tabs.misc
import tabs.npc
import tabs.probe
import tabs.race
import tabs.repair
import tabs.sound_gen
import tabs.sound
import tabs.spell
import tabs.static
import tabs.weapon

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Activators', value='tab-1'),
        dcc.Tab(label='Achemy', value='tab-2'),
        dcc.Tab(label='Apparatus', value='tab-3'),
        dcc.Tab(label='Armor', value='tab-4'),
        dcc.Tab(label='Book', value='tab-5'),
        dcc.Tab(label='Class', value='tab-6'),
        dcc.Tab(label='Clothing', value='tab-7'),
        dcc.Tab(label='Container', value='tab-8'),
        dcc.Tab(label='Enchanting', value='tab-9'),
        dcc.Tab(label='Ingredients', value='tab-10'),
        dcc.Tab(label='Leveled Creatures', value='tab-11'),
        dcc.Tab(label='Leveled Items', value='tab-12'),
        dcc.Tab(label='Light', value='tab-13'),
        dcc.Tab(label='Lockpick', value='tab-14'),
        dcc.Tab(label='Misc', value='tab-15'),
        dcc.Tab(label='NPC', value='tab-16'),
        dcc.Tab(label='Probe', value='tab-17'),
        dcc.Tab(label='Race', value='tab-18'),
        dcc.Tab(label='Repair', value='tab-19'),
        dcc.Tab(label='Sound Gen', value='tab-20'),
        dcc.Tab(label='Sound', value='tab-21'),
        dcc.Tab(label='Spell', value='tab-22'),
        dcc.Tab(label='Static', value='tab-23'),
        dcc.Tab(label='Weapon', value='tab-24'),
    ]),
    html.Div(id='tabs-example-content')
])

@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tabs.activators.activators_table
    elif tab == 'tab-2':
        return tabs.alchemy.alchemy_table
    elif tab == 'tab-3':
        return tabs.apparatus.apparatus_table
    elif tab == 'tab-4':
        return tabs.armor.armor_table
    elif tab == 'tab-5':
        return tabs.book.book_table
    elif tab == 'tab-6':
        return tabs.classes.class_table
    elif tab == 'tab-7':
        return tabs.clothing.clothing_table
    elif tab == 'tab-8':
        return tabs.container.container_table
    elif tab == 'tab-9':
        return tabs.enchanting.enchanting_table
    elif tab == 'tab-10':
        return tabs.ingredients.ingredients_table
    elif tab == 'tab-11':
        return tabs.leveled_creature.leveled_creature_table
    elif tab == 'tab-12':
        return tabs.leveled_item.leveled_item_table
    elif tab == 'tab-13':
        return tabs.light.light_table
    elif tab == 'tab-14':
        return tabs.lockpick.lockpick_table
    elif tab == 'tab-15':
        return tabs.misc.misc_table
    elif tab == 'tab-16':
        return tabs.npc.npc_table
    elif tab == 'tab-17':
        return tabs.probe.probe_table
    elif tab == 'tab-18':
        return tabs.race.race_table
    elif tab == 'tab-19':
        return tabs.repair.repair_table
    elif tab == 'tab-20':
        return tabs.sound_gen.sound_gen_table
    elif tab == 'tab-21':
        return tabs.sound.sound_table
    elif tab == 'tab-22':
        return tabs.spell.spell_table    
    elif tab == 'tab-23':
        return tabs.static.static_table
    elif tab == 'tab-24':
        return tabs.weapon.weapon_table

if __name__ == '__main__':
    app.run_server(debug=True)