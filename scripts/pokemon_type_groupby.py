from distutils.log import debug
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, dash_table, dcc  # pip install dash (version 2.0.0 or higher)
import plotly.express as px
from dash.dependencies import Input, Output

app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("data/pokemon.csv")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Pokemon Stats Dashboard created by Dash + plotly", style={'text-align': 'center'}),

    dcc.Dropdown(id="select_grpby",
                 options=[
                     {"label": "Type 1", "value": "Type 1"},
                     {"label": "Type 2", "value": "Type 2"},
                     {"label": "Generation", "value": "Generation"},
                     {"label": "Legendary", "value": "Legendary"}],
                 multi=False,
                 value="Type 1",
                 style={'width': "40%"}
                 ),
    dcc.Dropdown(id="select_y",
                 options=[
                     {"label": "Total", "value": "Total"},
                     {"label": "HP", "value": "HP"},
                     {"label": "Attack", "value": "Attack"},
                     {"label": "Defence", "value": "Defence"},
                     {"label": "Sp. Atk", "value": "Sp. Atk"},
                     {"label": "Sp. Def", "value": "Sp. Def"},
                     {"label": "Speed", "value": "Speed"}],
                 multi=False,
                 value="Total",
                 style={'width': "40%"}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='output_graph', figure={}),
    dcc.Dropdown(id="select_grpby2",
                 options=[
                     {"label": "Type 1", "value": "Type 1"},
                     {"label": "Type 2", "value": "Type 2"},
                     {"label": "Generation", "value": "Generation"},
                     {"label": "Legendary", "value": "Legendary"}],
                 multi=False,
                 value="Type 1",
                 style={'width': "40%"}
                 ),
    dcc.Dropdown(id="select_y2",
                 options=[
                     {"label": "Total", "value": "Total"},
                     {"label": "HP", "value": "HP"},
                     {"label": "Attack", "value": "Attack"},
                     {"label": "Defence", "value": "Defence"},
                     {"label": "Sp. Atk", "value": "Sp. Atk"},
                     {"label": "Sp. Def", "value": "Sp. Def"},
                     {"label": "Speed", "value": "Speed"}],
                 multi=False,
                 value="Total",
                 style={'width': "40%"}
                 ),
    html.Div(id='output_container2', children=[]),
    html.Br(),
    dcc.Graph(id='output_graph2', figure={})
    # dash_table.DataTable(id= 'table'),
    ])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='output_graph', component_property='figure'),
    Output(component_id='output_container2', component_property='children'),
    Output(component_id='output_graph2', component_property='figure')],
    [Input(component_id="select_grpby", component_property='value'),
     Input(component_id="select_y", component_property='value'),
     Input(component_id="select_grpby2", component_property='value'),
     Input(component_id="select_y2", component_property='value')]
)
def update_figure(slct_grp, slct_y, slct_grp2, slct_y2):
    container =  'graph 1 : ' + str(slct_grp) +" and " + str(slct_y) + " were selected respectively."
    df_groupby = df.groupby([slct_grp])[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].mean()
    df_groupby.reset_index(inplace=True)
    fig = go.Figure()
    fig = px.bar(df_groupby,
                 x= slct_grp,
                 y = slct_y)

    container2 =  'graph 2 : ' + str(slct_grp2) +" and " + str(slct_y2) + " were selected respectively."
    df_groupby2 = df.groupby([slct_grp2])[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].mean()
    df_groupby2.reset_index(inplace=True)
    fig2 = go.Figure()
    fig2 = px.bar(df_groupby2,
                 x= slct_grp2,
                 y= slct_y2)
    return container, fig, container2, fig2

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    server = app.server  #variable name serve is just an example. name it whatever...
    app.run_server(host='127.0.0.1',port=8700)
