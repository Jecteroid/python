#coding utf-8
import random
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

list_1 = [random.randint(1, 100) for _ in range(1, 10)]
print(f'Массив до замены мест макс и мин элементов списка - {list_1}')

max_i = list_1.index(max(list_1))
min_i = list_1.index(min(list_1))

list_1[max_i], list_1[min_i] = list_1[min_i], list_1[max_i]

print(f'Массив после замены - {list_1}')




