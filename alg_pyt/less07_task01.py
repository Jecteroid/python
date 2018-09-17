#coding utf-8

import random

len_arr = random.randint(1, 50)

array = [random.randint(-100, 99) for _ in range(len_arr)]

print(f'Исходный массив - {array}')


def puz_sort(array):

    n = 1
    while n < len(array):
        count_n = 0
        for i in range(len(array) - 1):

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count_n += 1

        if count_n == 0:
            break

        n += 1


puz_sort(array)

print(f'Массив после сортировки - {array}')