# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

score = 2021
candies_player1 = 0
candies_player2 = 0
min = 1
max = 28
flag = False


def check_win(step, player_name1, player_name2, whoCheck):
    global score
    global candies_player2
    global candies_player1
    global flag

    if (whoCheck == 'player_1' or whoCheck == 'player_2'):
        # проверяем на победу ход игрока 1
        if (whoCheck == 'player_1' and score <= 0):
            print(player_name1, "забирает", step + score, "конфет")
            candies_player1 += score
            print(player_name1, "победил!")
            print("----------------------------СЧЁТ---------------------------")
            print(player_name1, ":", candies_player1, "конфет ||", player_name2, ":", candies_player2, "конфет")
            print(player_name1, "получает все конфеты соперника, теперь у него", candies_player1 + candies_player2, "конфет!")
            return whoCheck

        # проверяем на победу ход игрока 2 (или компьютера)
        if (whoCheck == 'player_2' and score <= 0):
            print(player_name2, "забирает", step + score, "конфет")
            candies_player2 += score
            print(player_name2, "победил!")
            print("----------------------------СЧЁТ---------------------------")
            print(player_name1, ":", candies_player1, "конфет ||", player_name2, ":", candies_player2, "конфет")
            print(player_name2, "получает все конфеты соперника, теперь у него", candies_player1 + candies_player2, "конфет!")
            return whoCheck

    # если никто пока не победил, выводим счет (flag - индикатор того, что счет уже печатался в этом ходу)
    if (score > 0 and flag == False):
        print("У", player_name1, candies_player1, "конфет")
        print("У", player_name2, candies_player2, "конфет")
        print("В куче осталось", score, " конфет")
        return 0

def game(priority, player_1, player_2, mode):
    global score
    global candies_player1
    global candies_player2
    global min
    global max
    flag = False # сбрасываем флаг печати счёта

    if (priority == True):
        # ход игрока 2 (или компьютера) первый
        if (mode == 'pve'): step = randint(min, max) # если ходит компьютер
        if (mode == 'pvp'): # если ходит игрок
            step = 29
            while (step > 28):
                print("Введите количество конфет (не более 28), которое хотите забрать (", player_2, ")")
                step = int(input())
        print(chr(27) + "[2J") # очистка экрана 
        candies_player2 += step
        score -= step
        # если текущий ход был последний, то выходим из рекурсии
        flag = False # счет не выводим
        if (check_win(step, player_1, player_2, 'player_2') == 'player_2'):
            return
        print(player_2, "забирает", step, "конфет")
        
        # ход игрока 1
        step = 29
        while (step > 28):
            print("Введите количество конфет (не более 28), которое хотите забрать (", player_1, ")")
            step = int(input())
        print(chr(27) + "[2J") # очистка экрана
        candies_player1 += step
        score -= step
        # если текущий ход был последний, то выходим из рекурсии
        flag = True # печатаем счёт
        if (check_win(step, player_1, player_2, 'player_1') == 'player_1'):
            return
        print(player_1, "забирает", step, "конфет")

    else:
        # ход игрока 1
        step = 29
        while (step > 28):
            print("Введите количество конфет (не более 28), которое хотите забрать (", player_1, ")")
            step = int(input())
        print(chr(27) + "[2J") # очистка экрана
        candies_player1 += step
        score -= step
        # если текущий ход был последний, то выходим из рекурсии
        flag = False # не печатаем счёт
        if (check_win(step, player_1, player_2, 'player_1') == 'player_1'):
            return
        print(player_1, "забирает", step, "конфет")

        # ход игрока 2 (или компьютера) первый
        if (mode == 'pve'): step = randint(min, max) # если ходит компьютер
        if (mode == 'pvp'): # если ходит игрок
            step = 29
            while (step > 28):
                print("Введите количество конфет (не более 28), которое хотите забрать (", player_2, ")")
                step = int(input())
        print(chr(27) + "[2J") # очистка экрана 
        candies_player2 += step
        score -= step
        # если текущий ход был последний, то выходим из рекурсии
        flag = True # печатаем счёт
        if (check_win(step, player_1, player_2, 'player_2') == 'player_2'):
            return
        print(player_2, "забирает", step, "конфет")

    # запускаем игру в рекурсии пока кто-то не выйграет
    game(priority, player_1, player_2, mode)

# главный алгоритм
mode = 0
while (mode > 2 or mode == 0):
    print(chr(27) + "[2J")
    print("Выберите режим игры")
    print("1. Против компьютера | 2. Против другого игрока")
    mode = int(input())

if (mode == 1):
    print("------------------ИГРОК ПРОТИВ КОМПЬЮТЕРА------------------")
    botMode = 'выбор'
    while (not (botMode == 'легкий') and not (botMode == 'средний') and not (botMode == 'тяжелый') and not (botMode == 'хардкор')):
        print("Выберите режим игры против копмьютера (легкий, средний, тяжелый, хардкор)")
        botMode = input()

    # градация уровней сложности
    if (botMode == 'легкий'): 
        N = 1 # шанс, что игрок будет ходить первым 50%
        # компьютер выбирает случайно кол-во конфет от 0 до 10
        min = 1
        max = 10
    if (botMode == 'средний'): 
        N = 2 # шанс, что игрок будет ходить первым 33%
        # компьютер выбирает случайно кол-во конфет от 10 до 20
        min = 11
        max = 20
    if (botMode == 'тяжелый'): 
        N = 5 # шанс, что игрок будет ходить первым 17%        
        # компьютер выбирает случайно кол-во конфет от 10 до 20
        min = 21
        max = 28
    if (botMode == 'хардкор'): 
        N = 9 # шанс, что игрок будет ходить первым 10%        
        # компьютер выбирает случайно кол-во конфет от 10 до 20
        min = 26
        max = 28

    print("Введите Ваше имя")
    player_1 = input()
    player_2 = 'Компьютер'
    print(chr(27) + "[2J")
    print("-----------------------------------------------------------")
    if (randint(0,N) == 0):
        print("Первым ходит", player_1)
        firstMove = False
    else:
        print("Первым ходит", player_2)
        firstMove = True
    game(firstMove, player_1, player_2, 'pve')

if (mode == 2):
    print("------------------ИГРОК ПРОТИВ ИГРОКА------------------")
    print("Введите имя первого игрока")
    player_1 = input()
    print("Введите имя второго игрока")
    player_2 = input()
    print(chr(27) + "[2J")
    print("-------------------------------------------------------")
    if (randint(0,1) == 1):
        print("Первым ходит", player_1)
        firstMove = False
    else:
        print("Первым ходит", player_2)
        firstMove = True
    game(firstMove, player_1, player_2, 'pvp')