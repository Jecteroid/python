#coding utf-8

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

LIMIT_1 = 9
LIMIT_2 = 99

for i in range(2, LIMIT_1 + 1):
    count_num = 0
    for j in range(2, LIMIT_2 + 1):
        if j % i == 0:
            count_num += 1

    print(f'{count_num} чисел кратно {i}')

