#coding utf-8

import random

len_arr = random.randint(1, 20)

array = [random.randint(-100, 99) for _ in range(len_arr // 2 * 2 + 1)]

print(f'Исходный массив - {array}')


def med(array):
    array = array[:]

    if len(array) == 1:
        return array[0]

    array.remove(min(array))
    array.remove(max(array))

    return med(array)


mediana = med(array)

print(mediana)