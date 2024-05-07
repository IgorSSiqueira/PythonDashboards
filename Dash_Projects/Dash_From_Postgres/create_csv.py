import pandas as pd
from sqlalchemy import create_engine

import sys
sys.path.append(r'C:\Users\Desenv_IG\Documents\1 - Python')
from vendas_query import query

def get_csv():
    engine = create_engine('postgresql://postgres:123456@localhost/DB_IGOR?client_encoding=latin1')
        
    df = pd.read_sql(query, engine)
    engine.dispose()

    df.to_csv('vendas_cliente_NF.csv')
    df = pd.read_csv('vendas_cliente_NF.csv')
    df['dt_emissao'] = pd.to_datetime(df['dt_emissao'])
    df['mes_ano'] = df['dt_emissao'].apply(lambda x: '{:02d}'.format(x.month)) + df['dt_emissao'].apply(lambda x: '/{:04d}'.format(x.year))
    df['dia_mes_ano'] = df['dt_emissao'].apply(lambda x: '{:02d}'.format(x.day)) + df['dt_emissao'].apply(lambda x: '/{:02d}'.format(x.month)) + df['dt_emissao'].apply(lambda x: '/{:04d}'.format(x.year))
    df.to_csv('vendas_cliente_NF.csv')
    return pd.read_csv('vendas_cliente_NF.csv')