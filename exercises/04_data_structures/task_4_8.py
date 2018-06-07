# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
ip = IP.replace('.',",").split(',')
ip_template = '''
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b}   {1:08b}   {2:08b}   {3:08b}
'''
print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
