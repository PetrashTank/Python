# Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Введите длину шоколадки в дольках: "))
m = int(input("Введите ширину шоколадки в дольках: "))
k = int(input("Сколько долек хотите съесть?  "))
if k < m * n and (k % m == 0 or k % n == 0):
    print('Можно отломить шоколадку')
else:
    print('Нельзя отломить шоколадку')
