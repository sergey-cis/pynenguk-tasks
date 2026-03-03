# -*- coding: utf-8 -*-
"""
Завдання 6.2

Замінити у рядку line всі голосні у нижньому регістрі на голосні у верхньому
регістрі. Змінений рядок записати в змінну result і вивести стандартний потік
виведення (stdout) за допомогою print.

Приклад роботи завдання:
$ python task_6_2.py
GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s

Рядок line не можна змінювати вручну, всі зміни треба зробити за допомогою
Python.
"""
vowels = ["a", "o", "i", "u", "e", "y"]
line = "Guido van Rossum began working on Python in the late 1980s"

# Soulition without loops:
"""
print(line.strip(" ").rstrip().lstrip().replace(
    "a", "A").replace("o", "O",).replace("u", "U").replace("e", "E").replace("i", "I").replace("y", "Y"))
"""

# Solution with for loop
for l in line:
    if l in vowels:
        line = line.replace(l, l.upper())

result = line
print(result)
