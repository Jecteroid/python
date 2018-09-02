#coding utf-8

# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

ROW_MATRIX = 4
COL_MATRIX = 5

matrix_x = [[0] * COL_MATRIX for i in range(ROW_MATRIX)]

for i in range(0, ROW_MATRIX):
    for j in range(0, COL_MATRIX - 1):
        matrix_x[i][j] = int(input('Введите число: '))

    matrix_x[i][COL_MATRIX - 1] = sum(matrix_x[i])

for i in range(0, ROW_MATRIX):
    for j in range(0, COL_MATRIX):
        print(matrix_x[i][j], end=' ')
    print()
