#coding utf-8

# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число: '))

even_list = []
odd_list = []

num_all = num

while True:
    if num % 10 % 2 != 0:
        odd_list.append(num % 10)

    else:
        even_list.append(num % 10)

    if num // 10 == 0:
        break

    num = num // 10

dots = ', '
print(f'В числе {num_all} {len(even_list)} четные цифры(а) ({dots.join(map(str, even_list))}), {len(odd_list)} нечетные цифры(а) ({dots.join(map(str, odd_list))})')

