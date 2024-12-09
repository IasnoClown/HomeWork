# Задача "Распаковка"
def print_params(a = 1, b = 'строка', c = True): # Задача №1.1
    print(a, b, c) # Задача №1.2

print_params(5.1, 'слово', False) # Задача №1.3
print_params()
print_params(b = 25) # Задача №1.4
print_params(c = [1,2,3])
values_list = ['one', 9.5, False] # Задача №2.1
values_dict = {'a' : 5, 'b' : 4, 'c' :3} # Задача №2.2
print_params(*values_list) # Задача №2.3
print_params(**values_dict)
values_list_2 = ('Urban', 25) # Задача №3.1
print_params(*values_list_2) # Задача №3.2
