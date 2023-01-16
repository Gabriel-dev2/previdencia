from fastapi import APIRouter
from config.db import conn
from models.index import clientes
from schemas.index import Clientes

cliente = APIRouter(
    prefix='/add',
    tags=['cliente']
)

@cliente.post("/cliente")
async def cadastrar_cliente(cliente: Clientes):
    conn.execute(clientes.insert().values(
        cpf=cliente.cpf,
        nome=cliente.nome,
        email=cliente.email,
        dataDeNascimento=cliente.dataDeNascimento,
        sexo=cliente.sexo,
        rendaMensal=cliente.rendaMensal
    ))

    cliente_cadastrado = conn.execute(clientes.select().where(clientes.c.cpf == cliente.cpf)).fetchone()
    return {'id': cliente_cadastrado['id']}