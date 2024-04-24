import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6('Altere o valor abaixo para realizar o callback'),
    html.Div(['Entrada:',
              dcc.Input(id='my-input',
                        value='valor inicial',
                        type='text')]),
    html.Br(),
    html.Div(id='my-output'),
])

@app.callback(
    #output
    Output(
        component_id='my-output',
        component_property='children'
    ), 

    #inputs
    [Input(
        component_id='my-input',
        component_property='value'
    )],

    #states -> não será usado agora
    #[],
)
def update_output_div(value):
    return "Saída: {}".format(value)


if __name__ == "__main__":
    app.run_server(debug=True)