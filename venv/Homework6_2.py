"""2)	Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

class Massa(Road):
    def __init__(self, _length, _width, m_asf, polotno):
        super().__init__(_length, _width)
        self.polotno = polotno
        self.m_asf = m_asf

    def m(self):
        return self._length * self._width * self.polotno * self.m_asf

r = Massa(10, 2000, 0.025, 0.1)
print(r.m())

