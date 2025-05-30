"""Endpoint для вычесления квадратного уравнения"""
from fastapi import FastAPI
from logic import kv_ur

app = FastAPI()


@app.get("/quadratic_equation")
async def quadratic_equation(a: float, b: float, c: float):
    """Endpoint для вычесления квадратного уравнения"""
    massage = kv_ur(a, b, c)
    return {"Ответ": massage}
