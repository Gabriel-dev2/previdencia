from fastapi import APIRouter
from config.db import conn
from models.index import produtos
from schemas.index import Produtos

produto = APIRouter(
    prefix='/add',
    tags=['produto']
)

@produto.post('/produto')
async def cadastrar_produto(produto: Produtos):
    conn.execute(produtos.insert().values(
        nome=produto.nome,
        susep=produto.susep,
        expiracaoDeVenda=produto.expiracaoDeVenda,
        valorMinimoAporteInicial=produto.valorMinimoAporteInicial,
        valorMinimoAporteExtra=produto.valorMinimoAporteExtra,
        idadeDeEntrada=produto.idadeDeEntrada,
        idadeDeSaida=produto.idadeDeSaida,
        carenciaInicialDeResgate=produto.carenciaInicialDeResgate,
        carenciaEntreResgates=produto.carenciaEntreResgates
    ))

    produto_cadastrado = conn.execute(produtos.select().where(produtos.c.nome == produto.nome)).fetchone()
    return {'id': produto_cadastrado['id']}