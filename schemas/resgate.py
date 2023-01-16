from pydantic import BaseModel

class Resgate(BaseModel):
    idPlano: int
    valorResgate: float