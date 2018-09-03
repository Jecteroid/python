#coding utf-8
import random
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

list_1 = [random.randint(1, 100) for _ in range(1, 100)]

max_i = list_1.index(max(list_1))
min_i = list_1.index(min(list_1))

if max_i < min_i:
    sum_1 = sum(list_1[max_i + 1:min_i])

else:
    sum_1 = sum(list_1[min_i + 1:max_i])

print(f'Массив - {list_1}')
print(f'Сумма между минимальным и максимальным элементами - {sum_1}')

