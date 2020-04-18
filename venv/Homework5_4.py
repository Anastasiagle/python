"""4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
"""
file = open('text_5_4.txt')
text = file.readlines()
print(text)
file2 = open('copytext_5_4.txt','w')
for i in text:
    i = i.split()
    if int(i[2]) == 1:
        i[0] = 'Один'
        file2.write(str(i))
        file2.write('\n')
    elif int(i[2]) == 2:
        i[0] = 'Два'
        file2.write(str(i))
        file2.write('\n')
    elif int(i[2]) == 3:
        i[0] = 'Три'
        file2.write(str(i))
        file2.write('\n')
    elif int(i[2]) == 4:
        i[0] = 'Четыре'
        file2.write(str(i))
        file2.write('\n')
file.close()