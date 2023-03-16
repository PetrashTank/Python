# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# k = int(input("Введите до какого числа вывести степени 2 "))
# i = 0
# while 2 ** i <= k:
#   print(2 ** i)
#   i += 1

N = int(input('Введите число N '))
flag = 0
P = 2
for i in range(N):
    if flag != 1:
        P = P ** i
        if P <= N:
            print(P)
            P = 2
        else:
            flag = 1
    else:
        i = N
