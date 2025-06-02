from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str

# Rota raiz simples
@app.get("/")
async def root():
    return {"message": "Backend está rodando!"}

# Rota para listar itens
@app.get("/items", response_model=List[Item])
async def read_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]

# Rota para adicionar itens
@app.post("/items", response_model=Item)
async def add_item(item: Item):
    # Aqui só retorna o que recebeu, sem salvar (simplificado)
    return item
