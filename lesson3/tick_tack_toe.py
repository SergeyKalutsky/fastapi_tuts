import sys
import requests
from time import sleep

base_url = 'http://127.0.0.1:8000'

def create_board():
    return([['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']])
 
 
def board_to_string(board):
    string_board = '  0 1 2\n'
    for i, row in enumerate(board):
        string_board += str(i) + ' ' + ' '.join(row) + '\n'
    return string_board[:-1]
 
 
def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                continue
        if win:
            return win
    return win
 
 
def col_win(board, player):
    for x in range(len(board)):
        win = True
 
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win:
            return win
    return win
 
def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x][x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x][y] != player:
                win = False
    return win
 
 
def evaluate(board):
    winner = False
 
    for player in ['X', 'O']:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
 
            winner = player
 
    return winner
 
 
def place_board(col, row, sign, board):
    if col > 2 or row > 2 or row < 0 or col < 0:
        return board, 'Место за пределами доски'
    if board[col][row] != '.':
        return board, 'Место занято!'
    board[col][row] = sign
    return board, ''
 
 
def play_game():
    board, winner = create_board(), False
    print(board_to_string(board))
    sleep(2)
 
    res = requests.get(base_url + '/register_user')
    data = res.json()
    if data['status'] != 'ok':
        print('К сожалению, пока играть нельзя')
        return
    sign = data['message']
    while True:
        res = requests.post(base_url + '/play', json={'player': sign, 'board': board})
        winner = evaluate(board)
        if winner: 
            print('Победил:', winner + '                   ', end='\r')
            sleep(1)
            continue
        data = res.json()
        if data['status'] == 'wait':
            board = data['board']
            sys.stdout.write("\033[4F")
            print(board_to_string(board) + '\nОжидаем ход другого игрока...', end="\r")
            sleep(1)
            continue
        print()
        col = int(input('Выберите ряд: '))
        row = int(input('Выберите столбец: '))
        board, error = place_board(col, row, sign, board)
        print(board_to_string(board) + '\nОжидаем ход другого игрока...', end="\r")
        if error:
           print(error) 
           continue
 
play_game()