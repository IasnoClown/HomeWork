# Задача "Все ли равны?"
number1 = int(input('Введите число №1: ')) # first, second, third и zero
number2 = int(input('Введите число №2: '))
number3 = int(input('Введите число №3: '))
if number1 == number2 == number3:
    print('Third')
elif number1 == number2 or number1 == number3:
    print('Second')
elif number2 == number1 or number2 == number3:
    print('Second')
elif number3 == number1 or number3 == number2:
    print('Second')
else:
    print('Zero')