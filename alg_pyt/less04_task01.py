#coding utf-8
import cProfile
# Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых трех уроков.

def row_of_num(n):
    sum_1 = 0

    list_1 = [i for i in range(1, n + 1)]

    for i in list_1:
        sum_1 += i

    return sum_1

# 1    0.000    0.000    0.000    0.000 less04_task01.py:5(row_of_num)  100 loops, best of 3: 58.7 usec per loop       - 1000
# 1    0.000    0.000    0.001    0.001 less04_task01.py:5(row_of_num)  100 loops, best of 3: 676 usec per loop        - 10000
# 1    0.003    0.003    0.008    0.008 less04_task01.py:5(row_of_num)  100 loops, best of 3: 8.17 msec per loop       - 100000

def num_1(count, num):
    sum_1 = ''
    num_sum = 0
    list_1 = [i for i in range(1, count + 1)]

    for i in list_1:
        sum_1 += str(i)

    for i in sum_1:
        if num == int(i):
            num_sum += 1

    return num_sum

# 1    0.001    0.001    0.001    0.001 less04_task01.py:19(num_1)  100 loops, best of 3: 838 usec per loop       - 1000
# 1    0.010    0.010    0.010    0.010 less04_task01.py:19(num_1)  100 loops, best of 3: 10.1 msec per loop      - 10000
# 1    0.115    0.115    0.120    0.120 less04_task01.py:19(num_1)  100 loops, best of 3: 123 msec per loop       - 100000


def sum_num(num):
    sum_1 = 0

    while num:
        sum_1 += num % 10
        num = num // 10

    return sum_1

# 1    0.000    0.000    0.000    0.000 less04_task01.py:38(sum_num)    100 loops, best of 3: 22.7 usec per loop        - 4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

def main():
    count_n = int(input("Введите n: "))
    # num_n =  int(input("Введите цифру: "))
    print(sum_num(count_n))

# main()
# cProfile.run('main()')
