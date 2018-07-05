# coding utf-8

# Задача 1
bit = 1
get = True
tin = 'dek'
print(bit, get, tin)

get = input('Введите что-нибудь: ')
print(get)

# Задача 2
numb = int(input('Введите число: '))
numb += 2
print(numb)

# Задача 3
ege = int(input('Введите ваш возраст: '))
if ege < 18:
    print('Извините, пользование данным ресурсом только с 18 лет')
else:
    print('Доступ разрешен')
