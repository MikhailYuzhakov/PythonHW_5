# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

path = "C:\\Users\\YuzhakovMikhail\\Desktop\\GeekBrains\\Программист\\I_четверть_2022_год\\Python\\PythonHW_5\\Task4\\Task4.txt"

with open(path, mode='r', encoding='utf-8') as file:
    usrString = file.read()
print("Исходная строка", usrString)

def RLEcompression(usrStr): # функция для сжатия данных алгоритмом RLE
    lastChar = usrStr[0]
    i = 0
    rle0 = [] # список для хранения символа
    rle1 = [] # список для хранения кол-во повторов символа

    for char in usrStr: # перебираем исходную строку посимвольно
        if (char == lastChar): # при совпадени текущего и предыдущего символов прибавляем единицу к счетчику i
            i += 1
            lastChar = char
        else:
            rle0.append(lastChar) # при несовпаднии текущего и предыдущего символов добавляем в список rle0 - символ, в rle1 - счётчик
            rle1.append(i)
            i = 1
            lastChar = char
    # проделываем те же манипуляции вне цикла для обработки последних символов
    rle0.append(lastChar)
    rle1.append(i)
    return list(zip(rle0, rle1)) # возвращаем список кортежей из символа и кол-ва повторов

def RLErecovery(usrTuple):
    usrStr = ""
    for item in usrTuple: # перебираем все кортежи в списке
        for j in range(int(item[1])): # добавляем в строку символ стоящий на первом месте кортежа столько раз сколько считали из второго элемента кортежа
            usrStr += str(item[0])
    return usrStr

# тело программы
print(chr(27) + "[2J") # очистка экрана
print("Исходные данные:", usrString)
RLEdata = RLEcompression(usrString)
print("Сжатая RLE алгоритмом строка:", RLEdata)
recovData = RLErecovery(RLEdata)
print("Восстановленные данные:", recovData)

# проверяем работу алгоритма на правильность
if (recovData == usrString):
    print("Исходные и восстановленные данные совпадают.")
else:
    print("Произошла ошибка алгоритма! Исходные и восстановленные данные не совпадают.")
