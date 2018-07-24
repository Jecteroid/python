#coding utf-8

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:
    def __init__(self, name, color, type = 'животное'):
        self.name = name
        self.color = color
        self.type = type

    def Make_toy(self):
        print(f'============= Поступил заказ на изготовление игрушки {self.name}, тип - {self.type}, цвет - {self.color} =============\n')

        self.Purchase()
        self.Tailoring()
        self.Painting()

        print(f'\n============= Изготовление игрушки {self.name} окончено =============')

    def Purchase(self):
        print(f'Закупаем сырье для игрушки с типом {self.type}, {self.color} гаммы')

    def Tailoring(self):
        print(f'Ведется пошив игрушки {self.name}')

    def Painting(self):
        print(f'Окрашиваем игрушку {self.name} в {self.color} цвет')

bear = Toy('Миша', 'бурый', 'животное')

bear.Make_toy()

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toys:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def Make_toy(self):
        print(f'============= Поступил заказ на изготовление игрушки {self.name}, цвет - {self.color} =============\n')

        self.Purchase()
        self.Tailoring()
        self.Painting()

        print(f'\n============= Изготовление игрушки {self.name} окончено =============')

    def Purchase(self):
        print(f'Закупаем сырье для игрушки {self.name}, {self.color} гаммы')

    def Tailoring(self):
        print(f'Ведется пошив игрушки {self.name}')

    def Painting(self):
        print(f'Окрашиваем игрушку {self.name} в {self.color} цвет')

class Toys_animal(Toys):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'животное'

    def get_type(self):
        print(f'Тип игрушки - {self._type}')

class Toys_character(Toys):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'персонаж мультфильма'

    def get_type(self):
        print(f'Тип игрушки - {self._type}')

class Toys_factory:

    def __init__(self, type, name , color):
        self.type = type
        self.name = name
        self.color = color

    def type_of_toy(self):
        if self.type == 'животное':
            return Toys_animal(self.name, self.color)
        elif self.type == 'персонаж мультфильма':
            return Toys_character(self.name, self.color)
        else:
            print('Такой тип еще не поддерживается фабрикой игрушек')

bears = Toys_factory('животное', 'миша', 'бурый').type_of_toy()
bears.Make_toy()


