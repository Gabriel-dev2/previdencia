from pydantic import BaseModel

class Produtos(BaseModel):
    id: int
    nome: str
    susep: str
    expiracaoDeVenda: str
    valorMinimoAporteInicial: float
    valorMinimoAporteExtra: float
    idadeDeEntrada: int
    idadeDeSaida: int
    carenciaInicialDeResgate: int
    carenciaEntreResgates: int