# coding utf-8
import random
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь

rand1 = random.randrange(1, 8)

list1 = []
list2 = []

for i in range(rand1):
    val = int(input(f'Введите {i+1}(Целое число) из {rand1} элементов 1-ого списка: '))
    list1.append(val)

print('===== Исходный список =====')
print(f'1-ый: {list1}')

for i in range(rand1):
    if (list1[i] ** 0.5).is_integer() and list1[i] >= 0:
        list2.append(int(list1[i] ** 0.5))

print('===== Список после манепуляций =====')
print(f'2-ой: {list2}')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
listdd = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадцать четвёртое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']

listmm = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'сентебря', 'октября', 'октября', 'ноября', 'декабря']

str = input('Введите датy в формате dd.mm.yyyy: ')

dd, mm, yyyy = str.split('.')

dds = dd
mms = mm
yyyys = yyyy

dd = int(f'{dd}')
mm = int(f'{mm}')
yyyy = int(f'{yyyy}')

while dd > 31 or dd < 1 or mm > 12 or mm < 1 or dd == 31 and (mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11) or len(str) != 10 or len(dds) != 2 or len(mms) != 2 or len(yyyys) != 4:
    str = input('Введите датy в корректном формате dd.mm.yyyy: ')
    dd, mm, yyyy = str.split('.')

    dd = int(f'{dd}')
    mm = int(f'{mm}')
    yyyy = int(f'{yyyy}')

print(f'{listdd[dd - 1]} {listmm[mm - 1]} {yyyy} года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

listn = []

n = int(input('Введите сколько должно быть элементов в массиве: '))

for i in range(0, n):
    listn.append(random.randint(-100, 100))

print(f'Список: {listn}')

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]

rand1 = random.randrange(1, 8)

list1 = []
list2 = []

for i in range(rand1):
    val = input(f'Введите {i+1} из {rand1} элементов 1-ого списка: ')
    list1.append(val)

print('===== Исходный список =====')
print(f'1-ый: {list1}')

for val in list1:
    if list2.count(val) == 0:
        list2.append(val)

print('===== Неповторяющиеся элементы исходного списка из list1 =====')
print(f'2-ой: {list2}')

# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

rand1 = random.randrange(1, 8)

list1 = []
list2 = []

for i in range(rand1):
    val = input(f'Введите {i+1} из {rand1} элементов 1-ого списка: ')
    list1.append(val)

print('===== Исходный список =====')
print(f'1-ый: {list1}')

for val in list1:
    if list1.count(val) == 1:
        list2.append(val)

print('===== Элементы исходного списка, которые не имеют повторений из list1 =====')
print(f'2-ой: {list2}')

