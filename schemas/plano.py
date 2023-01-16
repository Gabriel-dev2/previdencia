from pydantic import BaseModel

class Plano(BaseModel):
    id: int
    idPlano: int
    idCliente: int
    saldo: float