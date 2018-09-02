#coding utf-8
import random
# Определить, какое число в массиве встречается чаще всего.

list_1 = [random.randint(1, 10) for _ in range(1, 10)]

max_count = max([list_1.count(x) for x in list_1])
max_count_x = 0

for x in list_1:
    if list_1.count(x) == max_count:
        max_count_x = x
        break

print(f'Массив - {list_1}')
print(f'{max_count_x} встречается чаще всего')

