immutable_var = 1, 2, True, False, 'Urban', 'Student' # Задание 2
print(immutable_var)
# immutable_var[0] = 5 # Задание 3 - Нельзя изменить кортеж, так как он не поддерживает изменение по элементам
# print(immutable_var)
mutable_list = [1, 2, 1.1, 2.2, True, False, 'Urban', 'Student']
mutable_list[0] = 5
mutable_list[2] = 100
mutable_list[4] = 'equally'
mutable_list.append('lesson')
print(mutable_list)
