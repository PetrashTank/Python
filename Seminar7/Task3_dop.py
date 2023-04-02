# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.


numbers = input('Введите список чисел через пробел: ')
int_array = [int(i) for i in numbers.split(' ') if i.isdigit()]


def filter_num(in_num):
    if (in_num >= 10) and (in_num <= 99) or (in_num <= -10) and (in_num > -100):
        return True
    else:
        return False


out_filter = filter(filter_num, int_array)

print("Все двузначные числа: ", " ".join(map(str, list(out_filter))))
