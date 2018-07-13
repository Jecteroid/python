# coding utf-8
import random

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
def damage(player1, player2):
    flag = False
    player2['healf'] -= player1['damage']

    if player2['healf'] < 0:
        player2['healf'] = 0
        flag = True

    return player1, player2, flag


quantity_players = int(input('Введите желаемое кол-во игроков(не меньше 2-ух): '))

if quantity_players < 2:
    print('Извините, но вы ввели некоректные данные xD')
    raise SystemExit

names = []

for player in range(1, quantity_players + 1):
    name = input(f'Введите имя {player}-го игрока: ')
    globals()[name] = {'name': name, 'healf': random.randint(100, 250),
                       'damage': random.randint(50, 180)}  # Создаем словарь вида 'player%i'
    names.append(name)

for player in range(1, quantity_players + 1):
    print(f'Имя {player}-го игрока: {names[player-1]}')

player_atack = input('Введите имя атакуещего игрока из списка выше: ')

player_def = input('Введите имя защищающегося игрока из списка выше: ')

player_atack, player_def, fl = damage(globals()[player_atack], globals()[player_def])

if fl:
    print(f'Игрок с именем {player_def["name"]} трагично умер')

else:
    print(f'Игрок с именем {player_def["name"]} ранен, но еще осталось {int(player_def["healf"])} hp')

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
def damageto(damage, armor):
    return damage / armor

def damage(player1, player2):
    damagetoplayer = damageto(player1['damage'], player2['armor'])
    flag = False
    player2['healf'] -= damagetoplayer

    if player2['healf'] < 0:
        player2['healf'] = 0
        flag = True

    return player1, player2, flag


quantity_players = int(input('Введите желаемое кол-во игроков(не меньше 2-ух): '))

if quantity_players < 2:
    print('Извините, но вы ввели некоректные данные xD')
    raise SystemExit

names = []
fl = 0
for player in range(1, quantity_players + 1):
    name = input(f'Введите имя {player}-го игрока: ')
    with open(f'{name}.txt', 'w', encoding='utf-8') as file_player:
        file_player.write(f'healf - {random.randint(100, 250)}\n')
        file_player.write(f'damage - {random.randint(50, 180)}\n')
        file_player.write(f'armor - {random.uniform(1, 4)}\n')

    globals()[name] = {'name': name}  # Создаем словарь вида 'player%i'

    with open(f'{name}.txt', 'r', encoding='utf-8') as file_player:
        _, globals()[name]['healf'] = file_player.readline().split(' - ')
        _, globals()[name]['damage'] = file_player.readline().split(' - ')
        _, globals()[name]['armor'] = file_player.readline().split(' - ')

        globals()[name]['healf'] = int(globals()[name]['healf'])
        globals()[name]['damage'] = int(globals()[name]['damage'])
        globals()[name]['armor'] = float(globals()[name]['armor'])

    names.append(name)
while fl == 0:
    for player in range(1, quantity_players + 1):
        print(f'Имя {player}-го игрока: {names[player-1]}')

    player_atack = input('Введите имя атакуещего игрока из списка выше: ')

    player_def = input('Введите имя защищающегося игрока из списка выше: ')

    player_atack, player_def, fl = damage(globals()[player_atack], globals()[player_def])

    if fl:
        pass

    else:
        print(f'Игрок с именем {player_def["name"]} ранен, но еще осталось {int(player_def["healf"])} hp')
        print('------- Продолжаем играть -------')

else:
    print('------- Игра окончена -------')
    print(f'Игрок с именем {player_def["name"]} трагично умер')
    print(f'Игрок с именем {player_atack["name"]} выиграл, у него осталось {int(player_atack["healf"])} hp')
    print('-----------------------------')
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
