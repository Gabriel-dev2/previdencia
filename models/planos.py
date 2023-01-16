from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import meta

planos = Table(
    'plano', meta,
    Column('id', Integer, primary_key=True),
    Column('idPlano', Integer),
    Column('idCliente', Integer),
    Column('saldo', Numeric())
)