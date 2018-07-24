#coding utf-8

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = False

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction = 'В неизвестном направлении'):
        return f'Машина повернула {direction}'

    def is_police(self):
        return self._is_police


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

# Случайно сразу так сделал))
