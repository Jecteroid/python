#coding utf-8
import struct
import sys
import ctypes
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)
# 1

count = int(input('Введите кол-во элементов ряда: '))

sum_1 = 0

for i in range(1, count + 1):
    sum_1 += float(input('Введите число: '))
    show_size(sum_1)

print(sum_1)

# 2

count = int(input('Введите кол-во элементов ряда: '))
num = int(input('Введите цифру, которую надо посчитать: '))

sum_1 = ''
num_sum = 0

for i in range(1, count + 1):
    sum_1 += input('Введите число: ')
    show_size(sum_1)

for i in sum_1:
    if num == int(i):
        num_sum += 1
        show_size(num_sum)

print(f'Цифра {num} встречается {num_sum} раз')


# 3

count = int(input('Введите кол-во элементов ряда: '))

sum = 0
max_sum = 0
max_num = 0

for i in range(1, count + 1):
    num = int(input('Введите натуральное число: '))
    num_safe = num

    while num:
        sum += num % 10
        num = num // 10
        show_size(sum)
        show_size(num)

    if sum > max_sum:
        max_sum = sum
        max_num = num_safe
        show_size(max_sum)
        show_size(max_num)

    sum = 0

print(f'Наибольшее по сумме цифр, является число {max_num}, сумма его цифр составляет {max_sum}')

# Все программы используют эффективные методы метод, но во второй задаче можно обойтись без строк, так получится эффективнее, считаю, что третья задача наиболее эффективно испольхует память