# Задача "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [4, 6, 8, 10]
not_primes = [3, 5, 7, 9, 11]
primes.clear() # Задание №1
not_primes.clear()
print(primes)
print(not_primes)
for i in numbers: # Задание №2
    print(i)
for i in numbers: # Задание №3
    for j in numbers:
        print(f'{i} / {j} = {i // j}')
def is_prime(num): # Задание №4
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    if is_prime(num):
        print(f"{num} Простое")
    else:
        print(f"{num} Не простое")
primes = [2, 3, 5, 7, 11, 13]
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
print('Простое числа: ', primes)
print('Не простые числа : ', not_primes)
