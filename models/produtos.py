from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import meta

produtos = Table(
    'produtos', meta,
    Column('id', Integer, primary_key=True),
    Column('nome', String(255)),
    Column('susep', String(255)),
    Column('expiracaoDeVenda', String(100)),
    Column('valorMinimoAporteInicial', Numeric()),
    Column('valorMinimoAporteExtra', Numeric()),
    Column('idadeDeEntrada', Integer),
    Column('idadeDeSaida', Integer),
    Column('carenciaInicialDeResgate', Integer),
    Column('carenciaEntreResgates', Integer)
)