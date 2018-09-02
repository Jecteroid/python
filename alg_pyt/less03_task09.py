#coding utf-8
import random
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

ROW_MATRIX = 4
COL_MATRIX = 5

matrix_x = [[random.randint(1, 100) for _ in range(COL_MATRIX)] for _ in range(ROW_MATRIX)]

for i in range(0, ROW_MATRIX):
    for j in range(0, COL_MATRIX):
        print(matrix_x[i][j], end=' ')
    print()

col_max_sum = []

for j in range(0, COL_MATRIX):
    col_sum = []
    for i in range(0, ROW_MATRIX):
        col_sum.append(matrix_x[i][j])

    col_max_sum.append(min(col_sum))

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы - {max(col_max_sum)}')