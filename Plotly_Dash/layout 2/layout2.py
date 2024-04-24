import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        id="dp-1",
        options=[
            {'label': 'Rio grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Paraná', 'value': 'PR'}],
        value="RS",
        style={"margin-bottom": "25px"}
    ),
    

    html.Label("Checklist"),
    dcc.Checklist(
        id="ck-1",
        options=[
            {'label': 'Rio grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Paraná', 'value': 'PR'}],
        value=["RS"],
        style={"margin-bottom": "25px"}
    ),

    html.Label("Input"),
    dcc.Input(
        value='SP', 
        type='text', 
        style={'margin-left': '10px'}
    ),

    html.Label('\nSlider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 8)},
        value=5,
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)