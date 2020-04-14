"""4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартанул'

    def stop(self):
        return f'{self.name} остановился'

    def turn_l(self):
        return f'{self.name} повернул налево'

    def turn_r(self):
        return f'{self.name} повернул направо'

    def show_speed(self):
        return f'{self.name} имеет скорость - {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} имеет скорость - {self.speed}')
        if self.speed > 40:
            return ('Скорость превышена')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} имеет скорость - {self.speed}')
        if self.speed > 60:
            return ('Скорость превышена')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a= SportCar(300, 'Зеленый', 'Феррари', 0)
b = TownCar(120, 'Синий', 'Форд', 0)
c = WorkCar(80, 'Желтый', 'Опель', 0)
d = PoliceCar(150, 'Черный',  'Ваз', 1)
print(a.show_speed())
print(c.turn_l())
print(f'{d.name} - {d.color}')


