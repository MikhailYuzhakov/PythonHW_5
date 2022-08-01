# Напишите программу, удаляющую из текста все слова, содержащие "абв".

phrase = ""
newPhrase = ""

with open('D:\Code\PythonHW_5\Task1\Task1.txt', mode='r', encoding='utf-8') as f:
    phrase = f.read()
print(phrase)
phrase = phrase.split()

for item in phrase:
    for i in range(len(item)-2):
        if (item[i] == 'а' and item[i+1] == 'б' and item[i+2] == 'в'): 
            print("Удалено слово", item)
            phrase.remove(item)
for item in phrase:
    newPhrase += item + " "

print(newPhrase)