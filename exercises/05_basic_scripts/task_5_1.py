# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
# Ну понятно, что "используя только пройденные темы" в этом задании делать нечего.
# На нашем уровне обучения, автор явно перегнул с заданием... 
# Про импорт мы тоже ничего еще не знаем. Поэтому, попробуем начать так:

def cidr_to_netmask(cidr):
  cidr = int(cidr)
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))

# взято из stackoverflow, которое упониналось в курсе.
# продолжаем детский сад:

our_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{4:}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:08b} {6:08b} {7:08b} {8:08b}
'''
net = input("insert network. format 10.1.1.0/24 : ").replace('.',",").replace('/',',').split(',')
mask = cidr_to_netmask(net[4]).replace('.',",").split(',')
netmask = net + mask
#print(our_template.format(int(netmask[0]), int(netmask[1]), int(netmask[2]), int(netmask[3]),  int(netmask[4]), int(netmask[5]), int(netmask[6]), int(netmask[7]), int(netmask[8])))
# Попробую уменьшить код.
netmask = [ int(x) for x in netmask if x.isdigit() ]
print(our_template.format( *netmask ))
#  и этого тоже нет в курсе...

# end
