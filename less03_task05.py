#coding utf-8
import random
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

list_1 = [random.randint(-100, 100) for _ in range(1, 100)]

max_minus_el = min([i for i in list_1 if i < 0])
max_minus_el_index = list_1.index(max_minus_el)

print(f'Массив - {list_1}')
print(f'Максимальный отрицательный элемент в массиве - {max_minus_el}, его позиция - {max_minus_el_index}')


