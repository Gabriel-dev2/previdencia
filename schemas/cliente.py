from pydantic import BaseModel

class Clientes(BaseModel):
    id: int
    cpf: str
    nome: str
    email: str
    sexo: str
    dataDeNascimento: str
    rendaMensal: float