from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()  # Crie a instância primeiro

# Depois aplique o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique o domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    start = time.perf_counter()
    end = time.perf_counter()
    duration_ms = round((end - start) * 1000, 2)
    return {
        "message": "pong",
        "response_time_ms": duration_ms,
        "server_time": time.time()
    }
