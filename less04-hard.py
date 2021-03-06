#codding utf-8

# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.\n''Остаток {}'.format(money, round(person['money'], 2))
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print('Ваш баланс:', check_account(person))
    elif choice == 2:
        fl = 1
        while fl:
            try:
                count = float(input('Сумма к снятию:'))

            except ValueError:
                print('Данные не в верном формате, попробуйте еще раз')

            else:
                fl = 0
                print(withdraw_money(person, count))

def start():
    fl = 1
    card_number = ''
    pin_code = ''

    while fl:
        try:
            card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
            card_number = int(card_number)
            pin_code = int(pin_code)

        except ValueError:
            print('Данные не в верном формате, попробуйте еще раз')

        else:
            fl = 0

    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = ''
            fl = 1

            while fl:
                ex = 1

                try:
                    choice = int(input('Выберите пункт:\n'
                                       '1. Проверить баланс\n'
                                       '2. Снять деньги\n'
                                       '3. Выход\n'
                                       '---------------------\n'
                                       'Ваш выбор:'))
                except ValueError:
                    print('Такого пункта нет, попробуйте еще раз')
                    ex = 0

                else:
                    fl = 0

                if choice != 1 and choice != 2 and choice != 3 and ex:
                    print('Такого пункта нет, попробуйте еще раз')
                    fl = 1

            if choice == 3:
                print('Вы вышли из симулятора банкомата')
                break
            process_user_choice(choice, person)
    else:
        print('Номер карты или пин код введены не верно!')


start()