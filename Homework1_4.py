# 4)	Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции

number = int(input('Введите целое положительное число:'))
max = 0
while number > 10:
    i = number % 10
    number //= 10
    if i > max:
        max = i
if number > max and i > number:
       max = i
if number > max and number> i:
       max = number
print('Самая большая цифра в числе: %d'%(max))



