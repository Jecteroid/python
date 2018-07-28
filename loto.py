# coding utf-8

from random import randint

# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

def gen_rand(list, start, stop):
    while True:
        rand_num = randint(start, stop)
        if rand_num not in list:
            list.append(rand_num)
            return rand_num


class Card:

    def __init__(self):
        self._list_num = []

    def get_list_num(self):
        return self._list_num

    def gen_str(self):
        str_num = []
        list_of_num = []

        for i in range(5):
            list_of_num.append(gen_rand(self.get_list_num(), 1, 90))

        list_of_num.sort()
        site_num_list = []

        for i in range(5):
            gen_rand(site_num_list, 0, 8)

        site_num_list.sort()

        for i in range(9):
            if i not in site_num_list:
                str_num.insert(i, '  ')

            if i < 5:
                if list_of_num[i] // 10:
                    str_num.insert(site_num_list[i], str(list_of_num[i]))

                else:
                    site_num_str = ' ' + str(list_of_num[i])
                    str_num.insert(site_num_list[i], site_num_str)

        str_num = ' '.join(str_num)
        return str_num

    def gen_card(self):
        card_str = f' {self.gen_str()} \n {self.gen_str()} \n {self.gen_str()} '
        self._list_num = []
        return card_str

class GameLoto:

    def __init__(self):
        self._card = Card()
        self._card_player = self._card.gen_card()
        self._card_robot = self._card.gen_card()
        self.list_used_keg = []

    def get_card_player(self):
        return self._card_player

    def get_card_robot(self):
        return self._card_robot

    def get_card(self):
        return self._card

    def gen_rand_keg(self):
        return gen_rand(self.list_used_keg, 1, 90)

    def is_number_in_card(self, num, card_anyone):
        return card_anyone.find(str(num))

    def is_win(self, card_anyone):
        for i in range(1, 91):
            if card_anyone.find(' '+str(i)+' ') != -1:
                return False

        return True

    def robot_card(self, keg):
        if self.is_number_in_card(' '+str(keg)+' ', self.get_card_robot()) != -1:
            if keg // 10:
                self._card_robot = self._card_robot.replace(' '+str(keg)+' ', '  - ')

            else:
                self._card_robot = self._card_robot.replace(' '+str(keg)+' ', ' - ')


    def game(self):

        while len(self.list_used_keg) != 90:
            keg = self.gen_rand_keg()
            print(f'Новый бочонок: {keg} (осталось {90 - len(self.list_used_keg)})')

            print(self.list_used_keg)

            print(' ------ Ваша карточка -----')
            print(self.get_card_player())
            print(' '+'-'*26)

            print(' -- Карточка компьютера ---')
            print(self.get_card_robot())
            print(' '+'-' * 26)

            ans = input('Зачеркнуть цифру? (y/n): ')


            self.robot_card(keg)

            if keg // 10 == 0:
                keg = ' ' + str(keg)

            if ans == 'Y' or ans == 'y':
                if self.is_number_in_card(' ' + str(keg) + ' ', self.get_card_player()) == -1:
                    print('Данной цифры нет на вашей карточке! Вы проиграли!')
                    return

                else:
                    self._card_player = self._card_player.replace(' ' + str(keg) + ' ', '  - ')

                    print('Цифра зачеркнута!')

                    if self.is_win(self.get_card_robot()):
                        print('Компьютер выиграл!!!')
                        return

                    if self.is_win(self.get_card_player()):
                        print('Ты выиграл!!!')
                        return


            elif ans == 'N' or ans == 'n':
                if self.is_number_in_card(' ' + str(keg) + ' ', self.get_card_player()) != -1:
                    print('Данная цифра есть на вашей карточке! Вы проиграли!')
                    return

                else:
                    print('Продолжаем играть!')

                    if self.is_win(self.get_card_robot()):
                        print('Компьютер выиграл!!!')
                        return

                    if self.is_win(self.get_card_player()):
                        print('Ты выиграл!!!')
                        return

            else:
                print('Такого ответа нет((')

                if self.is_win(self.get_card_robot()):
                    print('Компьютер выиграл!!!')
                    return

                if self.is_win(self.get_card_player()):
                    print('Ты выиграл!!!')
                    return

                return



game = GameLoto()
game.game()

