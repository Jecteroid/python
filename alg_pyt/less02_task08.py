#coding utf-8

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

count = int(input('Введите кол-во элементов ряда: '))
num = int(input('Введите цифру, которую надо посчитать: '))

sum = ''
num_sum = 0

for i in range(1, count + 1):
    sum += input('Введите число: ')

for i in sum:
    if num == int(i):
        num_sum += 1

print(f'Цифра {num} встречается {num_sum} раз')