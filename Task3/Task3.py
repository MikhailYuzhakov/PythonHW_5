# Создайте программу для игры в "Крестики-нолики"

from random import randint

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

if (randint(0,1) == 0): 
    flag = False
else: flag = True

def printBoard(board):
    print(chr(27) + "[2J") # очистка экрана 
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 0):
                print(" ", " ", end = '')
            if (board[i][j] == 1):
                print("X", " ", end = '')
            if (board[i][j] == -1):
                print("0", " ", end = '')
        print()

def checkWin():
    global board
    sum = 0

    for i in range(3): # проверяем каждый столбец  
        for j in range(3): 
            sum += board[i][j] 
        if (abs(sum) == 3): 
            print(abs(sum))
            return 1
    
    for i in range(3): # проверяем каждую строку
        for j in range(3): 
            sum += board[i][j]
        if (abs(sum) == 3): 
            print(abs(sum))
            return 1
    
    # проверяем диагонали
    if (abs(board[0][0] + board[1][1] + board[2][2]) == 3): 
        print(abs(sum))
        return 1
    if (abs(board[0][2] + board[1][1] + board[2][0]) == 3): 
        print(abs(sum))
        return 1

    return 0

def game():
    global flag
    printBoard(board)
    print(checkWin())
    if (flag):
        i = int(input())
        j = int(input())
        if (board[i][j] == 0): board[i][j] = 1
        flag = not flag
        if (checkWin()): 
            printBoard(board)
            print("Победили Х")
            return
        else:
            game()
            
    else:
        i = int(input())
        j = int(input())
        if (board[i][j] == 0): board[i][j] = -1
        
        flag = not flag
        if (checkWin()): 
            printBoard(board)
            print("Победили 0")
            return
        else:
            game()

game()

