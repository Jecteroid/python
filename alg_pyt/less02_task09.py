#coding utf-8

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

count = int(input('Введите кол-во элементов ряда: '))

sum = 0
max_sum = 0
max_num = 0

for i in range(1, count + 1):
    num = int(input('Введите натуральное число: '))
    num_safe = num

    while num:
        sum += num % 10
        num = num // 10

    if sum > max_sum:
        max_sum = sum
        max_num = num_safe

    sum = 0

print(f'Наибольшее по сумме цифр, является число {max_num}, сумма его цифр составляет {max_sum}')

