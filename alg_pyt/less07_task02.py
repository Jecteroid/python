#coding utf-8

import random

len_arr = random.randint(1, 50)

array = [random.uniform(0, 49) for _ in range(len_arr)]

print(f'Исходный массив - {array}')

def slit_sort(array):
    n = 0
    i = 0
    j = 0

    if len(array) <= 1:
        return

    m = len(array) // 2

    r_half = array[m:]
    l_half = array[:m]
    slit_sort(r_half)
    slit_sort(l_half)

    while i < len(l_half) and j < len(r_half):
        if l_half[i] < r_half[j]:
            array[n] = l_half[i]
            i += 1

        else:
            array[n] = r_half[j]
            j += 1

        n += 1

    while i < len(l_half):
        array[n] = l_half[i]
        i += 1
        n += 1

    while j < len(r_half):
        array[n] = r_half[j]
        j += 1
        n += 1

slit_sort(array)

print(f'Массив после сортировки - {array}')

