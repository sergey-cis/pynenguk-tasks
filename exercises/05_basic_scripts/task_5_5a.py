# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""

template = {"access": access_template, "trunk": trunk_template}
mode = input("Enter interface mode (access/trunk): ").lower()
interface = input("Enter interface type and number: ").capitalize()
# vlans = input("Enter VLAN(s) number: ")
if mode == "trunk":
    vlans = input('Enter the allowed VLANs:')
    print(f"interface {interface}")
    print(template[mode].format(vlans))
elif mode == "access":
    vlans = input('Enter VLAN number:')
    print(f"interface {interface}")
    print(template[mode].format(vlans))
