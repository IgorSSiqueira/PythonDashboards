import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div("Column"), style={'background': '#ff0000'},md=1),
        dbc.Col(html.Div("Column"), style={'background': '#ff00ff'}, md=4),
        dbc.Col(html.Div("Column"), style={'background': '#ffff00'}, md=7),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)