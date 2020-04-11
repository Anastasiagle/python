"""2)	Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""

file = open('text_5_2.txt')
text = file.read()
print(f'Вывод данных из файла: \n{text}')
file = open('text_5_2.txt')
text = file.readlines()
for i in range(len(text)):
    print(f'Всего слов в {i + 1} строке -  {len(text[i].strip())}')
print(f'Всего строк в файле - {i+1}')
file.close()