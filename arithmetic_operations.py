x = 2
y = 8
print(x + y)  # сложение
print(x + 3)
print(x - y)  # вычитание
print(x * y)  # произведение
print(x / y)  # деление
print(x // y) # целочисленное деление
print(x % y)  # остаток от деления
print(x ** y) # возведение в степень
print(3.2 * 0.8 - 2 * 5 - 3**3)  # арифметическое выражение
print(4 ** 0.5)  # возведение в степень 0.5 – квадратный корень

z = -2
print(abs(z))             # модуль числа
print(pow(z, 2), z ** 2)  # квадрат числа

m = 3.26
print(round(m), round(m, 1))  # округление числа до целого и до одного знака после запятой


import math  # импротируем модуль math

x = 3.265
# целое число, ближайшее целое снизу, ближайшее целое сверху
print(math.trunc(x), math.floor(x), math.ceil(x))

print(math.pi)  # константа пи
print(math.e)   # число Эйлера

y = math.sin(math.pi / 4)  # math.sin – синус
print(round(y, 2))

y = 1 / math.sqrt(2)  # math.sqrt – квадратный корень
print(round(y, 2))
