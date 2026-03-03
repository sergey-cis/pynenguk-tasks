# -*- coding: utf-8 -*-
"""
Завдання 6.6a

Зробити копію скрипта завдання 6.6.

Додати перевірку введеної IP-адреси.
Адреса вважається коректно заданою, якщо вона:
- складається з 4 чисел (а не літер чи інших символів)
- числа розділені точкою
- кожне число в діапазоні від 0 до 255

Якщо адреса неправильна, виводьте повідомлення: "Wrong IP address".  Якщо
адреса правильна, перевіряти та виводити тип адреси як у завданні 6.6.

Повідомлення "Wrong IP address" має виводитися лише один раз, навіть якщо
кілька пунктів вище не виконано.


Приклад виконання скрипту:
$ python task_6_6a.py
Enter IP address: 10.10.1.1
unicast

$ python task_6_6a.py
Enter IP address: 10.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: a.a.10.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.a.a
Wrong IP address

$ python task_6_6a.py
Enter IP address: 10,1,1,1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 500.1.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.1.1.1
Wrong IP address
"""
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

# Final Output
if not valid:
    print("Wrong IP address")
else:
    f_oct, s_oct, th_oct, fo_oct = int(parts[0]), int(
        parts[1]), int(parts[2]), int(parts[3])

    if 1 <= f_oct <= 223:
        print("unicast")
    elif 224 <= f_oct <= 239:
        print("multicast")
    elif f_oct == s_oct == th_oct == fo_oct == 255:
        print("local broadcast")
    elif f_oct == s_oct == th_oct == fo_oct == 0:
        print("unassigned")
    else:
        print("unused")
