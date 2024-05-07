# Dashboard feito de um arquivo .csv criado a partir de uma consulta SQL (Postgres)
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from app import app
df = pd.read_csv(r'C:\Users\Desenv_IG\Documents\1 - Python\PythonDashboards\Dash_Projects\Dash_From_Postgres\vendas_cliente_NF.csv')
df['dt_emissao'] = pd.to_datetime(df['dt_emissao'])


df_sales_per_month = df.groupby(df['mes_ano'])['valor_total'].sum()

sales_per_month_graph = px.bar(df_sales_per_month, 
                            x=df_sales_per_month.index, 
                            y='valor_total', 
                            labels={'valor_total': 'Total de Vendas', 'mes_ano': 'Mês/Ano'},
                            height= 200)
# sales_per_month = px.bar(df_sales_per_month, 
#                             x='valor_total',
#                             y=df_sales_per_month.index,  
#                             labels={'valor_total': 'Total de Vendas', 'mes_ano': 'Mês/Ano'}, 
#                             orientation='h')

#chamar no call back
# sales_per_month_graph.update_layout(title='Vendas por Mês/Ano',
#                                 xaxis_title='Mês/Ano',
#                                 yaxis_title='Total de Vendas')

#### Montando gráfico qtd itens vendidos por NF (bar vertical)
df_items_per_day = df.groupby(df['mes_ano'])['quantidade'].sum().reset_index()

items_per_day_graph = px.bar(df_items_per_day, 
                                x='quantidade', 
                                y='mes_ano', 
                                labels={'quantidade_item': 'Quantidade de Itens Vendidos', 'mes_ano': 'Data'},
                                orientation='h',
                                height= 480)


#### Montando gráfico venda por cliente (Pie)
data_pie = df.groupby('cod_clifor')['valor_total'].sum().reset_index()

pie_graph = px.pie(data_pie, 
                    labels=data_pie['cod_clifor'], 
                    values=data_pie['valor_total'],
                    hover_data=['cod_clifor', 'valor_total'],
                    hole=0.3,
                    height=200)

df_sales_day_per_month = df.groupby('dia_mes_ano')['valor_total'].sum()

sales_day_per_month_graph = px.line(df_sales_day_per_month,
                                        x=df_sales_day_per_month.index,
                                        y='valor_total',
                                        labels={'valor_total': 'Total de Vendas', 'dia_mes_ano': 'Dia/Mês/Ano'},
                                        height=200)

app.layout = html.Div([
    dbc.Row([
        #CONFIGURAÇÕES
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H4('By: Igor S. Siqueira'),
                ]),
                dbc.CardBody([
                    html.H3('Configurações'),
                    html.H5([
                        'Em andamento...'
                    ])
                ])
                
            ], style={'height': '90vh'})
        ], md=3),
        
        dbc.Col([
            #Gráfico barra - Venda mês - height ?            
            dbc.Row([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5('Vendas por mês'),
                    ]),
                    dbc.CardBody([
                        dcc.Graph(id='vendas_mes', figure=sales_per_month_graph),
                    ]),
                    
                
                ], style={'height': '30vh'}), 
            ]),
            
            
            dbc.Row([
                #Graph barras vertical - vendas Itens
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.H5('Qtde itens vendidos')
                        ]),
                        dbc.CardBody([
                            dcc.Graph(id='items_graph', figure=items_per_day_graph),
                        ]),
                        
                    ], style={'height': '60vh', 'margin-top': '5px'}),
                ], sm=4),
                
                dbc.Col([
                    #Graph Pie - Vendas clientes
                    dbc.Row([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5('Venda por cliente')
                            ]),
                            dbc.CardBody([
                                dcc.Graph(id='pie_graph', figure=pie_graph),
                            ]),
                        ], style={'height': '30vh'},),
                    ]),
                    
                    #Graph linha vendas diárias mensal
                    dbc.Row([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5('Venda por cliente')
                            ]),
                            dbc.CardBody([
                                dcc.Graph(id='sales_day_month_year', figure=sales_day_per_month_graph)
                            ]),
                            
                        ], style={'height': '30vh'},),
                    ]),
                        
                ], sm=8),
            ])
        ], sm=9),
    ])
])
if __name__ == '__main__':
    app.run_server(debug=False,port=8080,host='0.0.0.0')