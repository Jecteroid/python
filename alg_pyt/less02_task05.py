#coding utf-8

# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

FIRST_SYMBOL = 32
LAST_SYMBOL = 127

i = 1

for symbol in range(FIRST_SYMBOL, LAST_SYMBOL + 1):
    if i < 10:
        print(f'{symbol}-{chr(symbol)}', end=', ')
        i += 1
    else:
        print(f'{symbol}-{chr(symbol)}')
        i = 1


