# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных
import re


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Изменить абонента из справочника\n"
          "7. Закончить работу")


def change_person(old_name, new_name):
    person = read_csv()
    with open('phonebook.csv', "rt", encoding="utf-8") as fin:
        data_1 = fin.read()
        for row in person:

            if old_name == row[0] or old_name == row[2]:
                data_1 = data_1.replace(row[0], new_name)
                fin = open('phonebook.csv', "wt", encoding="utf-8")
                fin.write(data_1)
                print("Абонент изменен")
                break
        else:
            print("Абонент не найден")

    return old_name, new_name


def read_csv(filename='phonebook.csv'):
    """Функция читает csv-файл и возвращает список списков - строк csv-файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            data.append(line.strip('\n').split(','))
    return data


def display_all_records():
    """Функция выводит на печать содержание всего справочника в отформатированном виде."""
    data = read_csv()
    for row in data:
        print(
            f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_last_name():
    """Функция запрашивает фамилию абонента, находит данные по этой фамилии и выводит их на печать."""
    last_name = input('Введите фамилию: ')
    data = read_csv()
    for row in data:
        if row[0] == last_name:
            print(
                f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')
        else:
            print("Абонент не найден")


def delete_person():
    last_name = input('Введите фамилию: ')
    pattern = re.compile(re.escape(last_name))
    with open('phonebook.csv', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
                f.truncate()
        print("Абонент удален")


def find_phone_number():
    """Функция запрашивает телефон абонента, находит соответствующие данные и выводит на печать"""
    phone = input('Введите номер телефона: ')
    data = read_csv()
    for row in data:
        if row[2] == phone:
            print(
                f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')
        elif row[2] != phone:
            print("Абонент не найден")


def add_data(filename='phonebook.csv'):
    """Функция дополняет телефонный справочник данными нового абонента."""
    with open(filename, 'a', encoding='utf-8') as file:
        info = input(
            'Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
        file.write(','.join(info) + '\n')
        print('Данные записаны.')


show_menu()
number = 0
while number != '7':
    number = input()
    if number == '1':
        display_all_records()

    elif number == '2':
        find_last_name()

    elif number == '3':
        find_phone_number()

    elif number == '4':
        add_data()

    elif number == '5':
        delete_person()

    elif number == '6':
        old_name = input(
            'Введите фамилию абонента или номер телефона, которые необходимо изменить?: ')
        new_name = input(
            'Введите фамилию абонента или номер телефона, НА которые необходимо изменить?: ')
        change_person(old_name, new_name)


else:
    print('Работа завершена.')
