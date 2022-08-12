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
    html.H1("test", style={'text-align': 'center'}),
    dcc.Dropdown(id="select_grpby",
                 options=[
                     {"label": "Type 1", "value": "Type 1"},
                     {"label": "Type 2", "value": "Type 2"},
                     {"label": "Generation", "value": "Generation"},
                     {"label": "Legendary", "value": "Legendary"}],
                 multi=False,
                 value="Legendary",
                 style={'width': "40%"}
                 ),
    # html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='output_graph', figure={})
    # dash_table.DataTable(id= 'table'),
    ])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='output_graph', component_property='figure')],
    [Input(component_id="select_grpby", component_property='value')]
)
def update_figure(slct_grp):
    # container = "The group chosen by user was: {}".format(slct_grp)
    df_type1_groupby = df.groupby([slct_grp])[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].mean()
    df_type1_groupby.reset_index(inplace=True)
    fig = go.Figure()
    fig = px.bar(df_type1_groupby,
                 x= slct_grp,
                 y = 'Total')
    # return container, fig
    return fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    server = app.server  #variable name serve is just an example. name it whatever...
    app.run_server(host='127.0.0.1',port=8700)
