# Задача "Нули ничто, отрицание недопустимо!"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
posit = 0
while int < len(my_list):
    if my_list[posit] < 0:
        posit += 1
        continue
    print(my_list[posit])
    posit += 1
    if my_list[posit] < 0:
else:
    print('Положительные числа закончились')
