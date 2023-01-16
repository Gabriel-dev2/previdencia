from fastapi import FastAPI
from routes.index import cliente
from routes.index import produto
from routes.index import plano

app = FastAPI()

app.include_router(cliente)
app.include_router(produto)
app.include_router(plano)
