# Команда для запуска
# python -m uvicorn chat_api:app --reload 
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()


class Message(BaseModel):
    player: str
    board: list[list]


class GameSettings:
    user_count = 0
    signs = {0: 'X', 1: 'O'}
    current_player = 'X'
    board = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]


def board_changed(board1, board2):
    for i in range(len(board1)):
        for j in range(len(board1[0])):
            if board1[i][j] != board2[i][j]:
                return True
    return False


gs = GameSettings()


@app.get("/register_user")
async def save():
    if gs.user_count > 1:
        return {'status': 'error', 'message': 'failed, all users are set'}    
    sign = gs.signs[gs.user_count]
    gs.user_count += 1
    return {'status': 'ok', 'message': sign}


@app.post('/play')
async def create_user(msg: Message):
    if gs.current_player != msg.player and board_changed(msg.board, gs.board):
        gs.current_player = 'O' if gs.current_player == 'X' else 'X'
        return {'status': 'wait', 'board': gs.board}
    if gs.current_player != msg.player:
        return {'status': 'wait', 'board': gs.board}
    if not board_changed(msg.board, gs.board):
        return {'status': 'game'}
    gs.board = msg.board
    return {'status': 'wait', 'board': gs.board}