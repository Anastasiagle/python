"""4)	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. """

class Sklad:
    def __init__(self, name, price, kolvo):
        self.name = name
        self.price = price
        self.kolvo = kolvo

class Printer(Sklad):
    def print(self):
        return f'printing...'

class Scanner(Sklad):
    def scan(self):
        return f'scanning...'

class Xerox(Sklad):
    def xerox1(self):
        return f'copy...'

a = Printer('aaa', 5000, 2)
b = Scanner('bbb', 7000, 3)
c = Xerox('ccc', 3000, 4)
print(a.print())
print(b.scan())
print(c.xerox1())

