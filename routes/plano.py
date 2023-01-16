from fastapi import APIRouter, status, HTTPException
from config.db import conn
from models.index import contratacao_plano, clientes, produtos, planos, resgate_historico
from schemas.index import ContratacaoPlano, Plano, AporteExtra, Resgate, ResgateHistorico
from datetime import date, datetime
from decimal import Decimal

plano = APIRouter(
    prefix='/plano',
    tags=['plano']
)

@plano.post('/contratar')
async def contratar_plano(contratacao: ContratacaoPlano):
    cliente = conn.execute(clientes.select().where(clientes.c.id == contratacao.idCliente)).fetchone()
    
    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Cliente não encontrado'
        )
    
    
    produto = conn.execute(produtos.select().where(produtos.c.id == contratacao.idProduto)).fetchone()
    
    if produto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado'
        )

    expiracaoDeVenda = datetime.strptime(produto['expiracaoDeVenda'], '%Y-%m-%d')
    dataDaContrFormatada = datetime.strptime(contratacao.dataDaContratacao, '%Y-%m-%d')

    if expiracaoDeVenda.date() < dataDaContrFormatada.date():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Produto fora do período de venda'
        )
        
    if produto['valorMinimoAporteInicial'] > contratacao.aporte:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Aporte menor que o valor minimo'
        )

    anoNascimento = cliente['dataDeNascimento']

    idade = date.today().year - anoNascimento.year
    
    if produto['idadeDeEntrada'] > idade:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Idade não corresponde com a minima'
        )
        
    if produto['idadeDeSaida'] < idade:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Idade não corresponde com a maxima para saida'
        )
    
    conn.execute(contratacao_plano.insert().values(
        idCliente=contratacao.idCliente,
        idProduto=contratacao.idProduto,
        aporte=contratacao.aporte,
        dataDaContratacao=contratacao.dataDaContratacao
    ))
    
    plano_contratado = conn.execute(contratacao_plano.select().order_by(contratacao_plano.c.id.desc())).fetchone()
 
    conn.execute(planos.insert().values(
        idPlano=plano_contratado['id'],
        idCliente=contratacao.idCliente,
        saldo=contratacao.aporte
    ))
    
    return {'id': plano_contratado['id']}


@plano.put('/aporte/{id}')
async def aporte_extra(id: int, aporte: AporteExtra):
    plano_aporte = conn.execute(planos.select().where(planos.c.id == id)).fetchone()
    
    if plano_aporte is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Plano não encontrado'
        )
        

    if plano_aporte.saldo == 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Plano cancelado'
        )
          
    plano_contratado = conn.execute(contratacao_plano.select().where(contratacao_plano.c.id == plano_aporte.idPlano)).fetchone()
    produto_aporte = conn.execute(produtos.select().where(produtos.c.id == plano_contratado['idProduto'])).fetchone()
    
    if produto_aporte['valorMinimoAporteExtra'] < aporte.valorAporte:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Valor de aporte minimo não alcançado'
        )

    novo_saldo = plano_aporte['saldo'] + Decimal(aporte.valorAporte)
    
    conn.execute(planos.update().values(
        saldo=novo_saldo
        ).where(planos.c.id == id))
    
    return {'id': plano_aporte.id}


@plano.post('/resgate')
async def resgate_plano(resgate: Resgate):
    plano_resgate = conn.execute(planos.select().where(planos.c.id == resgate.idPlano)).fetchone()
    
    if plano_resgate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Plano não encontrado'
        )
    
    if plano_resgate.saldo == 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Plano cancelado'
        )
        
    plano_contratado = conn.execute(contratacao_plano.select().where(contratacao_plano.c.id == plano_resgate.idPlano)).fetchone()
    produto_resgate = conn.execute(produtos.select().where(produtos.c.id == plano_contratado['idProduto'])).fetchone()
    
    resgate_hist = conn.execute(resgate_historico.select().where(resgate_historico.c.idPlanoContratado == resgate.idPlano)).fetchone()
    
    delta = date.today() - plano_contratado['dataDaContratacao']

    
    if delta.days < produto_resgate['carenciaInicialDeResgate']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Prazo de 60 dias de carência não alcançado'
        )
    
    if plano_resgate['saldo'] < resgate.valorResgate:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Saldo menor que o valor a desejado para resgate'
        )
    
    if resgate_hist is not None:
        
        diff = resgate_hist.dataResgate - plano_contratado['dataDaContratacao']

        if produto_resgate['carenciaEntreResgates'] < diff.days:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Prazo fora do limite de carência entre resgates'
        )
        
        conn.execute(resgate_historico.update().values(
            idPlanoContratado=plano_resgate.id,
            dataResgate=datetime.strftime(date.today(), '%Y-%m-%d')
        ).where(resgate_historico.c.id == resgate_hist.id))
        
    novo_saldo = plano_resgate['saldo'] - Decimal(resgate.valorResgate)
    
    conn.execute(planos.update().values(
        saldo=novo_saldo
        ).where(planos.c.id == resgate.idPlano))
    
    conn.execute(resgate_historico.insert().values(
        idPlanoContratado=plano_resgate.id,
        dataResgate=datetime.strftime(date.today(), '%Y-%m-%d')
    ))
    
    return {'id': plano_resgate.id}