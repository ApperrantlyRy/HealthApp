# main.py

from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/ping")
async def ping():
    start = time.perf_counter()
    # Simular processamento (opcional)
    # time.sleep(0.05)  # 50ms, pode comentar se quiser resposta instantânea
    end = time.perf_counter()
    duration_ms = round((end - start) * 1000, 2)
    return {"message": "pong", "response_time_ms": duration_ms, "server_time": time.time()}
