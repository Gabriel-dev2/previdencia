from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import meta

clientes = Table(
    'clientes', meta,
    Column('id', Integer, primary_key=True),
    Column('cpf', String(100)),
    Column('nome', String(255)),
    Column('email', String(255)),
    Column('sexo', String(50)),
    Column('dataDeNascimento', String(100)),
    Column('rendaMensal', Numeric()),
)