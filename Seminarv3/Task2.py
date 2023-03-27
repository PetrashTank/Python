# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример: *

# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
N = int(input('Введите количество элементов в массиве A: '))
A = []
for i in range(N):
    A.append(randint(0, 100))
print(A)

X = int(input('Введите к какому числу нужно найти самое ближайшее (от 0 до 100): '))
min = abs(X - A[0])
index = 0
for i in range(1, N):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {X - A[index]}')
