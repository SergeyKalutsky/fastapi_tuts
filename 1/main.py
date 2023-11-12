# Команды для установки
# python -m pip install "fastapi[all]" --user
# pip install uvicorn

# Команда запуска
# python -m uvicorn main:app --reload


# Команда запуска  python -m uvicorn main:app --reload
from fastapi import FastAPI
from random import randint

app = FastAPI()

# curl http://127.0.0.1:8000 <- команда для вызова. Можно также скопировать в браузер без curl
@app.get("/")
async def root():
    return {"message": "Hello World"}

# curl 'http://127.0.0.1:8000/sum?x=10&y=20' <- команда для вызова. Можно также скопировать в браузер без curl
@app.get("/sum")
async def sum_vals(x: int = 0, y: int = 0):
    return {"Sum": x + y}

# Задания
# 1. Написать генератор случайных чисел
# Решение
# curl 'http://127.0.0.1:8000/random?min=10&max=20' <- команда для вызова. Можно также скопировать в браузер без curl
@app.get("/random")
async def sum_vals(min: int, max: int):
    return {"random number": randint(min, max)}

storage = {}
# curl 'http://127.0.0.1:8000/put?key=foo&val=bar' <- команда для вызова. Можно также скопировать в браузер без curl
# 2. key-value store написать хранилище данных
@app.get("/put")
async def sum_vals(key: str, val: str):
    storage[key] = val
    return {"message": 'success'}

# curl 'http://127.0.0.1:8000/get?key=foo'
@app.get("/get")
async def sum_vals(key: str):
    if key in storage:
        storage[key]
        return {"value": storage[key]}
    return {'message': 'error: Key is not found'}
