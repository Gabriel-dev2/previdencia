from pydantic import BaseModel

class AporteExtra(BaseModel):
    idCliente: int
    idPlano: int
    valorAporte: float