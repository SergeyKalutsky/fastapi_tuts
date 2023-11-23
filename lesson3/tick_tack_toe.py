import random
from time import sleep
 
 
def create_board():
    return([['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']])
 
 
def print_board(board):
    print('  0 1 2')
    for i, row in enumerate(board):
        print(i, ' '.join(row))
    
 
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
    print_board(board)
    sleep(2)
 
    sign = 'X'
    while not winner:
        col = int(input('Выберите ряд: '))
        row = int(input('Выберите столбец: '))
        board, error = place_board(col, row, sign, board)
        print_board(board)
        if error:
           print(error) 
           continue
        sign = 'X' if sign == 'O' else 'O'
        winner = evaluate(board)
    print(winner)
 
play_game()