from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir acesso do frontend (ajuste o domínio conforme seu deploy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para teste, depois coloque seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_db = []

@app.get("/items")
def read_items():
    return fake_db

@app.post("/items")
def add_item(item: dict):
    fake_db.append(item)
    return {"message": "Item added", "item": item}
