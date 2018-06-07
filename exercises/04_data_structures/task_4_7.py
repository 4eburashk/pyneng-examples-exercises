# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
mac_16 = MAC.replace(':',",").split(',')
print(mac_16)
mac_int = [ int(m,16) for m in mac_16 ]
print(mac_int)
mac_bin = '{:b} {:b} {:b}'.format(mac_int[0],mac_int[1],mac_int[2])
print(mac_bin)


