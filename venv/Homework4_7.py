"""7)	Реализовать генератор с помощью функции с ключевым словом yield,создающим очередное значение.
    При вызове функции должен создаваться объект-генератор.
    Функция должна вызываться следующим образом: for el in fact(n).
        Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
    Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

def generator(n):
    el=1
    m=1
    while el < n:
        m = m*(el+1)
        el+=1
        #print(m)
    yield m
fact=generator(4)
for i in fact:
    print(i)

#fact(4) = generator(n)
#for i in fact(4):
 #   print(i)
#fact=generator(4)

#g = fact(4)
#for i in g:
#    print(i)
#g = generator()

"""
def generator():
     for el in (10, 20, 30):
         yield el
#
g = generator()
#
#
for i in g:
     print(i)
"""