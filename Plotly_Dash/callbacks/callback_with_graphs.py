import dash
from dash import html, dcc
from dash.dependencies import Input, Output#, State
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(
        filtered_df, x='gdpPercap', y='lifeExp',
        size='pop', color='continent', hover_name='country',
        log_x=True, size_max=55) 

    fig.update_layout(transition_duration=1000)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)