from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from app import app
from _map import *   # noqa: F403
from _histogram import *    # noqa: F403
from _controllers import *  # noqa: F403

df_data = pd.read_csv('D:\Python\PythonDashboards\Dash_Projects\Venda_Imoveis\dataset\cleaned_data.csv')
mean_lat = df_data['LATITUDE'].mean()
mean_long = df_data['LONGITUDE'].mean()

df_data['size_m2'] = df_data['GROSS SQUARE FEET'] / 10.764
df_data = df_data[df_data['YEAR BUILT'] > 0]
df_data['SALE DATE'] = pd.to_datetime(df_data['SALE DATE'])

df_data.loc[df_data['size_m2'] > 10000, 'size_m2'] = 10000
df_data.loc[df_data['SALE PRICE'] > 50000000, 'SALE PRICE'] = 50000000
df_data.loc[df_data['SALE PRICE'] < 100000, 'SALE PRICE'] = 100000

# ===== LAYOUT =====
app.layout = dbc.Container([
        dbc.Row([
                dbc.Col([controllers], md=3), 
                dbc.Col([map, hist], md=9),
        ])
], fluid=True, )


# ===== CALBACKS =====

# def update_hist(location, square_size, color_map):


if __name__ == '__main__':
    app.run_server(debug=True)