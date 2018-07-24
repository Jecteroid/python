#coding utf-8

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, health, damage, armor):
        self.health = float(health)
        self.damage = float(damage)
        self.armor = float(armor)

    def _damage_received_by_rival(self, rival):
        return self.damage / rival.armor

    def atack_rival(self, rival):
        rival.health -= self._damage_received_by_rival(rival)
        rival.health = round(rival.health)

        if rival.health < 0:
            rival.health = 0


class Game:

    def __init__(self, attacker, defender):
        self.attaker = attacker
        self.defender = defender

    def game_process(self):
        self.attaker.atack_rival(self.defender)

        if self.defender.health == 0:
            return f'{self.defender.name} умер'

        else:
            return f'{self.defender.name} - {round(self.defender.health)} hp\n' \
            f'{self.attaker.name} - {round(self.attaker.health)} hp'

class Player(Person):

    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)
        self.name = 'Player'


class Enemy(Person):

    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)
        self.name = 'Enemy'

player = Player(100, 50, 1.7)

enemy = Enemy(80, 60, 1.4)

players = ['player', 'enemy']
print(players[1])

while player.health != 0 and enemy.health != 0:

    name_attaker = input('Введите имя атакующего игрока: ')
    if name_attaker not in players:
        continue

    name_defender = input('Введите имя защищающегося игрока: ')
    if name_defender not in players:
        continue

    name_attaker = globals()[name_attaker]
    name_defender = globals()[name_defender]

    game_result = Game(player, enemy)

    print(game_result.game_process())

else:
    print('Игра окончена!')

