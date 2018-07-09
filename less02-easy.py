# coding utf-8
import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruit = ["яблоко", "банан", "киви", "арбуз"]
for i in range(len(fruit)):
    print(f'{i+1}. {fruit[i]}')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

rand1 = random.randrange(1, 8)
rand2 = random.randrange(1, 8)

list1 = []
list2 = []

for i in range(rand1):
    val = input(f'Введите {i+1} из {rand1} элементов 1-ого списка: ')
    list1.append(val)

for i in range(rand2):
    val = input(f'Введите {i+1} из {rand2} элементов 2-ого списка: ')
    list2.append(val)

print('===== Исходные списки =====')
print(f'1-ый: {list1}')
print(f'2-ой: {list2}')

for val in list1:
    if list2.count(val):
        list1.remove(val)

print('===== Списки после удаления одинаковых элементов из list1 =====')
print(f'1-ый: {list1}')
print(f'2-ой: {list2}')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

rand1 = random.randrange(1, 8)

list1 = []

for i in range(rand1):
    val = int(input(f'Введите {i+1}(Целое число) из {rand1} элементов 1-ого списка: '))
    list1.append(val)

print('===== Исходные список =====')
print(f'1-ый: {list1}')

for i in range(rand1):
    if list1[i] % 2:
        # list1.insert(i, list1[i] * 2)
        # list1.remove(list1[i+1])
        list1[i] *= 2

    else:
        # list1.insert(i, list1[i] / 4)
        # list1.remove(list1[i+1])
        list1[i] /= 4


print('===== Список после манепуляций =====')
print(f'1-ый: {list1}')