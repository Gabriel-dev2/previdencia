from pydantic import BaseModel

class ResgateHistorico(BaseModel):
    id: int
    idPlanoContratado: int
    dataResgate: str