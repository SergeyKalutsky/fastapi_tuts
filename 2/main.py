from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    name: str
    message: str | None = None


app = FastAPI()

async def save_message(item: Item):
    print(item)
    with open('messages.txt', 'a+', encoding='utf-8') as f:
        date = datetime.now().strftime(r'%m/%d/%Y, %H:%M:%S')
        f.write(f'{date} {item.name}: {item.message}\n')

async def read_messages():
    with open('messages.txt', 'r', encoding='utf-8') as f:
        return f.read()

# http://127.0.0.1:8000/save_message
@app.post("/save_message/")
async def save(item: Item):
    await save_message(item)
    return {'message': 'success'}

@app.get("/messages/")
async def read():
    msgs = await read_messages()
    return msgs