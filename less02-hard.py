# coding utf-8

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y
equation = input('Введите формулу уравнения прямой: ')

x = input('Введите координату x: ')
equation = list(equation)

xi = equation.index('x')

equation.pop(xi)
equation.insert(xi, f' * {x}')

pi = equation.index('=')
equation = equation[pi+2:]

equation = eval(''.join(equation))

print(f'Координата y: {equation}')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

str = input('Введите датy в формате dd.mm.yyyy: ')

dd, mm, yyyy = str.split('.')

dds = dd
mms = mm
yyyys = yyyy

dd = int(f'{dd}')
mm = int(f'{mm}')
yyyy = int(f'{yyyy}')

while dd > 31 or dd < 1 or mm > 12 or mm < 1 or dd == 31 and (
        mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11) or len(str) != 10 or len(dds) != 2 or len(
        mms) != 2 or len(yyyys) != 4:
    str = input('Введите датy в корректном формате dd.mm.yyyy: ')
    dd, mm, yyyy = str.split('.')

    dd = int(f'{dd}')
    mm = int(f'{mm}')
    yyyy = int(f'{yyyy}')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
n = int(input('Введите имя комнаты: '))
k = 1
while n > k * (k + 1) * (2 * k + 1) // 6:
    k += 1

else:
    floor = (k ** 2 - k) // 2
    num = n - k * (k - 1) * (2 * k - 1) // 6
    sc = num % k
    if sc == 0:
        sc = k
        floor -= 1
    floor += num // k + 1

print(floor, sc)
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
