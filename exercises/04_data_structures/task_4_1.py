# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку NAT таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
print(NAT)
ss = NAT.split(' ')
ss[-2] = ss[-2].replace('Fast', 'Gigabit')
NAT = ' '.join(ss)
print(NAT)
# или так
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT)
print(NAT.replace('Fast', 'Gigabit'))


#end
