# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Введите число для преобразования: '))
n = list(map(lambda i: n//(2**abs(i))%2, [i for i in range(-7, 1)]))
print(*n)
