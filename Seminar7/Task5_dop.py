# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
lst = (input("Введите список слов через пробел: "))
lst_1 = lst.split(' ')
find = str(input("Что ищем? "))
num = 0
# def my_func(lst_1, find_str):
#     if lst_1.count(find_str) > 1:
#         k = lst_1.index(find_str)
#         print(lst_1.index(find_str, k+len(find_str)))
#     else:
#         print("Такого значения нет в списке ")

for i in range(len(lst_1)):
    if lst_1[i] == find:
        num += 1
        if num == 2:
            print(i)

if num == 1:
    print(f"Слово {find} встречается всего один раз ")
elif find not in lst_1:
    print("Такого значения нет в списке ")


# my_func(lst_1, f)
# lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# f = "йцу"
# my_func(lst, f)
# lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# f = "йцу"
# my_func(lst, f)
# lst = ["123", "234", 123, "567"]
# f = "123"
# my_func(lst, f)
# lst = []
# f = "123"
# my_func(lst, f)
