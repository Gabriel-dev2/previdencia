from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

resgate_historico = Table(
    'resgate_historico', meta,
    Column('id', Integer, primary_key=True),
    Column('idPlanoContratado', Integer),
    Column('dataResgate', String(100))
    )