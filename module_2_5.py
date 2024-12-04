# Задача "Матрица воплоти"
def get_matrix(n, m, value): # Задание №1
    matrix = [] # Задание №2
    if n <= 0 or m <= 0:
        return matrix

    for i in range(n): # Задание №3
        row = [] # Задание №4
        for j in range(m): # Задание №5
            row.append(value) # Задание №6
        matrix.append(row) # Задание №7

    return matrix

parameter1 = get_matrix(7, 3, 14)
parameter2 = get_matrix(6, 12, 9)
parameter3 = get_matrix(5, 9, 2)

print(parameter1) # Задание №8
print(parameter2)
print(parameter3)
