"""1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка."""

file = open('text.txt', 'w')
text = input('Введите текст:')
while text:
    file.writelines(text)
    text = input('Введите текст:')
    if not text:
        break
file.close()
file = open('text.txt', 'r')
print(file.readlines())
file.close()