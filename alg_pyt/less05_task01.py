#coding utf-8
from collections import namedtuple
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

enterprises = []

count_ent = int(input('Введите кол-во предприятий: '))

Enterprise = namedtuple('Enterprise', 'name qua_1 qua_2 qua_3 qua_4')

sum_1 = 0

for i in range(count_ent):
    ent = [input('Введите имя предприятия: '), int(input('Введите прибыль за первый квартал: ')), int(input('Введите прибыль за второй квартал: ')), int(input('Введите прибыль за третий квартал: ')), int(input('Введите прибыль за четвертый квартал: '))]
    enterprises.append(Enterprise._make(ent))
    sum_1 += enterprises[i].qua_1 + enterprises[i].qua_2 + enterprises[i].qua_3 + enterprises[i].qua_4

print(f'Средняя прибыль {sum_1 / count_ent}')

print('Предприятия, чья прибыль выше среднего: ')

for i in range(count_ent):
    if enterprises[i].qua_1 + enterprises[i].qua_2 + enterprises[i].qua_3 + enterprises[i].qua_4 > sum_1 / count_ent:
        print(enterprises[i].name)

print('Предприятия, чья прибыль ниже среднего: ')

for i in range(count_ent):
    if enterprises[i].qua_1 + enterprises[i].qua_2 + enterprises[i].qua_3 + enterprises[i].qua_4 < sum_1 / count_ent:
        print(enterprises[i].name)










