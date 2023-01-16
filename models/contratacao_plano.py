from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import meta

contratacao_plano = Table(
    'contratacao_plano', meta,
    Column('id', Integer, primary_key=True),
    Column('idCliente', Integer),
    Column('idProduto', Integer),
    Column('aporte', Numeric()),
    Column('dataDaContratacao', String(100)),
)