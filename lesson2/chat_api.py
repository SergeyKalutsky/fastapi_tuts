# Команда для запуска
# python -m uvicorn chat_api:app --reload 
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()

class User(BaseModel):
    name: str | None = None


class Message(BaseModel):
    user_id: int
    text: str | None = None


users = {}

async def save_message(msg: Message):
    with open('messages.txt', 'a+', encoding='utf-8') as f:
        date = datetime.now().strftime(r'%m/%d/%Y, %H:%M:%S')
        f.write(f'{date} {users[msg.user_id]}: {msg.text}\n')


async def read_messages():
    with open('messages.txt', 'r', encoding='utf-8') as f:
        return f.read()


@app.post("/save_message/")
async def save(msg: Message):
    await save_message(msg)
    return {'status': 'ok', 'message': 'success'}


@app.get("/messages/")
async def read():
    msgs = await read_messages()
    return msgs


@app.post('/create_user')
async def create_user(user: User):
    if user.name not in users.values():
        if len(users) == 0:
            user_id = 1
        else:
            user_id = max(users.keys()) + 1
        users[user_id] = user.name
        return {'status': 'ok', 'message': 'Пользователь создан успешно', 'user_id': user_id}
    return {'status':'error', 'message': 'Пользователь с такими именем уже существует'}