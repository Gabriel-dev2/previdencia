from pydantic import BaseModel

class ContratacaoPlano(BaseModel):
    id: int
    idCliente: int
    idProduto: int
    aporte: float
    dataDaContratacao: str