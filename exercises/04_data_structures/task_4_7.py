# -*- coding: utf-8 -*-
"""
Завдання 4.7

Перетворити MAC-адресу в рядку mac на двійковий рядок такого виду:
'101010101010101010111011101110111100110011001100'

Отриманий новий рядок вивести стандартний потік виведення (stdout) за допомогою
print.

Підказка: MAC-адреса без: це шістнадцяткове число AAAABBBBCCCC.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""
mac = "AAAA:BBBB:CCCC"

bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))
print(bin_mac)

# My solution
# """
# template = """
# First = {: ^ 08b}
# Second = {: ^ 08b}
# Third = {: ^ 08b}
# Fifth = {: ^ 08b}
# Sixth = {: ^ 08b}
# Seven = {: ^ 08b}
# Eigth = {: ^ 08b}
# inth = {: ^ 08b}
# Tenth = {: ^ 08b}
# Elev = {: ^ 08b}
# Fourth = {: ^ 08b}
# Twelve = {: ^ 08b}
# """
# mac = "AAAA:BBBB:CCCC"
# new_mac = (" ").join(mac.replace(":", "")).split()
# print(template.format(int(new_mac[0], 16), int(new_mac[1], 16),
#              int(new_mac[2], 16), int(new_mac[3], 16),
#              int(new_mac[4], 16), int(new_mac[5], 16),
#              int(new_mac[6], 16), int(new_mac[7], 16),
#              int(new_mac[8], 16), int(new_mac[9], 16),
#              int(new_mac[10], 16), int(new_mac[11], 16)))
# """
