# -*- coding: utf-8 -*-
"""
Завдання 6.6b

Зробити копію скрипта завдання 6.6a.
Доповнити скрипт: якщо адреса була введена неправильно, запитати адресу знову.

Якщо адреса неправильна, виводьте повідомлення: 'Wrong IP address'.
Повідомлення "Wrong IP address" має виводитися лише один раз після кожного
введення адреси, навіть якщо кілька пунктів перевірки адреси не виконано
(приклад виведення нижче).

Приклад виконання скрипту:
$ python task_6_6b.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: a.a.a
Wrong IP address
Enter IP address: 10.1.1.1.1
Wrong IP address
Enter IP address: 500.1.1.1
Wrong IP address
Enter IP address: a.1.1.1
Wrong IP address
Enter IP address: 50.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: 10.a.1.1.1
Wrong IP address
Enter IP address: 255.255.255.255
local broadcast

"""
while True:
    ip = input("Enter IPv4 address: ").strip()
    valid = True
    parts = ip.split(".")

    # Check length and number of parts
    if (len(ip) < 7 or len(ip) > 15) or (len(parts) != 4):
        valid = False

    # Check allowed characters
    if valid:
        for ch in ip:
            if not (ch.isdigit() or ch == "."):
                valid = False
                break

    # Validate octets
    if valid:
        for part in parts:
            if part == "":
                valid = False
                break
            if not part.isdigit():
                valid = False
                break
            number = int(part)
            if number < 0 or number > 255:
                valid = False
                break
            if len(part) > 1 and part[0] == "0":
                valid = False
                break

    if not valid:
        print("Wrong IP address")
    else:
        break   # exit loop when IP is correct

# Determine type (runs only when valid)

f_oct, s_oct, th_oct, fo_oct = int(parts[0]), int(
    parts[1]), int(parts[2]), int(parts[3])

if f_oct == s_oct == th_oct == fo_oct == 255:
    print("local broadcast")
elif f_oct == s_oct == th_oct == fo_oct == 0:
    print("unassigned")
elif 224 <= f_oct <= 239:
    print("multicast")
elif 1 <= f_oct <= 223:
    print("unicast")
else:
    print("unused")
