"""1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

class Date1:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def izvl(cls, day_month_year):
        my_list = []
        for i in day_month_year.split():
            if i != '-':
                my_list.append(i)
        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    @staticmethod
    def validation(day, month, year):
        if day<1 or day>31:
            return f'Ошибка в дне'
        if month<1 or month>12:
            return f'Ошибка в месяце'

    def __str__(self):
        return f'{Date1.izvl(self.day_month_year)}'


print(Date1.izvl('11 - 11 - 2011'))
print(Date1.validation(1, 20, 2020))




