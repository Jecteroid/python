#coding utf-8
import random
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

list_1 = [random.randint(1, 10) for _ in range(1, 10)]

print(f'Массив - {list_1}')

try:
    min_num_1 = min(list_1)
    list_1.remove(min(list_1))
    min_num_2 = min(list_1)
except ValueError:
    print('В массиве не хватает элементов')

else:
    print(f'Два наименьших элемента в массиве - {min_num_1}, {min_num_2}')