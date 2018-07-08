# coding utf-8

# Задача 1
numb = int(input('Введите число в диапазоне (0, 10): '))
while numb >= 10 or numb <= 0:
    if numb >= 10 or numb <= 0:
        print('Число неверное')
        numb = int(input('Введите число в диапазоне (0, 10): '))
else:
    print(numb ** 2)

# Задача 2
var_1 = input('Введите что-нибудь: ')
var_2 = input('Введите еще чего-нибудь: ')

var_1, var_2 = var_2, var_1
print('После замены значений:', var_1, var_2)

