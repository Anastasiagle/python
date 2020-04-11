# 2)	Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

input_sec = int(input('Введите время в секундах: '))
hour = int(input_sec / 60 / 60) % 24
min = int(input_sec / 60) % 60
sec = input_sec % (60)
if hour < 10:
    hour = str('0' + str(hour))
else:
    hour = str(hour)
if min < 10:
    min = str('0' + str(min))
else:
    min = str(min)
if sec < 10:
    sec = str('0' + str(sec))
else:
    sec = str(sec)
print('%s:%s:%s' % (hour, min, sec))
