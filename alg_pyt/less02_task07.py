#coding utf-8

# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

print('----- Проверяем равенство 1+2+...+n = n(n+1)/2 -----')

n = int(input('Введите n: '))

sum1 = 0
sum2 = int(n * (n + 1) / 2)

for i in range(1, n + 1):
    sum1 += i

sum1 = int(sum1)

print('+'.join(map(str, [i for i in range(1, n + 1)])), '=', sum1)
print('n(n+1)/2 =', sum2)
print('==>', end=' ')

if sum1 == sum2:
    print('+'.join(map(str, [i for i in range(1, n + 1)])), '= n(n+1)/2')
    print('Равенство верно!!!')
else:
    print('Равенство неверно!!!')

print('----- Проверка равенства завершена -----')