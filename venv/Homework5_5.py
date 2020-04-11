"""5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

def sum1():
            file = open('Number.txt','w')
            text = input('Введите набор чисел через пробел:')
            file.writelines(text)
            number = text.split()
            print(sum(map(int, number)))
            file.close()
sum1()