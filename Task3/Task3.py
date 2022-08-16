# Создайте программу для игры в "Крестики-нолики"

from random import randint

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # виртуальное игровое поле

if (randint(0,1) == 0): # выбираем очередность хода
    flag = False
else: flag = True

# функция для печать игрового поля
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

# функция проверяет условие победы
def checkWin():
    global board
    global flag
    
    sum = 0
    for i in range(3): # проверяем каждую строку  
        for j in range(3): 
            sum += board[i][j]      
        # print("Сумма по строкам:", sum)
        
        if (sum == -3):
            printBoard(board)
            print("Победили 0")
            return
        if (sum == 3):
            printBoard(board)
            print("Победили X")
            return
        sum = 0 # обнуляем переменную для следующем итерации
    
    sum = 0
    for i in range(3): # проверяем каждую столбец
        for j in range(3): 
            sum += board[j][i]
        # print("Сумма по столбцам", sum)

        if (sum == -3):
            printBoard(board)
            print("Победили 0")
            return
        if (sum == 3):
            printBoard(board)
            print("Победили X")
            return
        sum = 0 # обнуляем переменную для следующем итерации
    
    # проверяем диагонали
    sum = 0
    if (board[0][0] + board[1][1] + board[2][2] == -3):
        # print("Сумма по гл. диагоналям", board[0][0] + board[1][1] + board[2][2])
        printBoard(board)
        print("Победили 0")
        return
    if (board[0][0] + board[1][1] + board[2][2] == 3):
        # print("Сумма по гл. диагоналям", board[0][0] + board[1][1] + board[2][2])
        printBoard(board)
        print("Победили X")
        return
    
    sum = 0
    if (board[0][2] + board[1][1] + board[2][0] == -3):
        # print("Сумма по втор. диагоналям", board[0][2] + board[1][1] + board[2][0]) 
        printBoard(board)
        print("Победили 0")
        return
    if (board[0][2] + board[1][1] + board[2][0] == -3):
        # print("Сумма по втор. диагоналям", board[0][2] + board[1][1] + board[2][0]) 
        printBoard(board)
        print("Победили X")
        return

    flag = not flag # передаем ход ноликам
    game() # если никто не победил запускаем игру

def game():
    global flag
    printBoard(board) # печатаем игровое поле

    if (flag): # первые ходят крестики
        print("Ходят крестики. Ввелите позицию строки и столбца через Enter:")
        i = int(input()) # считываем позицию строки
        while (i > 2 or i < 0): # проверка на корректность введенных данных
            print("Такой позиции на игровом поле нет. Введите позицию строки и столбца через Enter:")
            i = int(input()) # считываем позицию строки

        j = int(input()) # считываем позицию столбца
        while (j > 2 or j < 0): # проверка на корректность введенных данных
            print("Такой позиции на игровом поле нет. Введите позицию строки и столбца через Enter:")
            j = int(input()) # считываем позицию строки
        
        if (board[i][j] == 0): board[i][j] = 1 # если поле не заполнено, то вписываем крестик (лог. 1)
        
        checkWin() # проверяем условие победы (передать флаг в качестве ключа)
            
    else: # первые ходят нолики
        print("Ходят нолики. Введите позицию строки и столбца через Enter:")
        i = int(input()) # считываем позицию строки
        while (i > 2 or i < 0): # проверка на корректность введенных данных
            print("Такой позиции на игровом поле нет. Введите позицию строки и столбца через Enter:")
            i = int(input()) # считываем позицию строки

        j = int(input()) # считываем позицию столбца
        while (j > 2 or j < 0): # проверка на корректность введенных данных
            print("Такой позиции на игровом поле нет. Введите позицию строки и столбца через Enter:")
            j = int(input()) # считываем позицию столбца

        if (board[i][j] == 0): board[i][j] = -1 # если поле не заполнено, то вписываем крестик (лог. -1)

        checkWin() # проверяем условие победы (передать флаг в качестве ключа)

game()

