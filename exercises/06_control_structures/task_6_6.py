# -*- coding: utf-8 -*-
"""
Завдання 6.6

Запросити користувача ввести IP-адресу у форматі 10.0.1.1
Залежно від типу адреси (описані нижче), вивести на стандартний потік виведення:
* 'unicast' - якщо перший байт у діапазоні 1-223 (приклад адреси 50.1.1.1)
* 'multicast' - якщо перший байт у діапазоні 224-239 (приклад адреси 224.1.1.1)
* 'local broadcast' - якщо IP-адреса дорівнює 255.255.255.255
* 'unassigned' - якщо IP-адреса дорівнює 0.0.0.0
* 'unused' - у всіх інших випадках

Приклад виконання скрипту:
$ python task_6_6.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6.py
Enter IP address: 224.1.1.1
multicast

$ python task_6_6.py
Enter IP address: 0.0.0.0
unassigned

$ python task_6_6.py
Enter IP address: 255.255.255.255
local broadcast

$ python task_6_6.py
Enter IP address: 250.1.1.1
unused

"""
get_ip = input("Enter IP address: ")
oct_ip = get_ip.strip().split(".")

if int(oct_ip[0]) >= 1 and int(oct_ip[0]) < 223:
    print("unicast")
elif int(oct_ip[0]) <= 239 and int(oct_ip[0]) > 224:
    print("multicast")
elif int(oct_ip[0]) == int(oct_ip[1]) == int(oct_ip[2]) == int(oct_ip[3]) == 255:
    print('local broadcast')
elif int(oct_ip[0]) == int(oct_ip[1]) == int(oct_ip[2]) == int(oct_ip[3]) == 0:
    print('unassigned')
else:
    print("unused")
