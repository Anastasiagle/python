# 3)	Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#    Напишите решения через list и через dict.

"""month = int(input('Введите порядковый номер месяца: '))
winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
if (month in winter):
    print('Winter')
elif (month in spring):
    print('Spring')
elif (month in summer):
    print('Summer')
elif (month in autumn):
    print('Autumn')
else:
    print('Error. Please try again')
"""


month = input('Введите порядковый номер месяца: ')
a = {'12':'Winter','1':'Winter','2':'Winter','3':'Spring','4':'Spring','5':'Spring', '6':'Summer','7':'Summer','8':'Summer','9':'Autumn','10':'Autumn','11':'Autumn'}
if month in a:
    print(a.get(month))
else:
    print('Error. Please Try again')
