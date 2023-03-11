from os import path

file_base = "phonebook.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    # Считывание данных из базы

    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])

        return all_data


def show_all():
    # Отображение содержимого базы данных

    if not all_data:
        print("Телефонная книга пуста\n")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    # Добавление новой записи

    global last_id

    array = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись успешно добавлена!\n")
    else:
        print("Данные уже существуют!")


def del_contact():
    # Удаление записи

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите id записи: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Некорректные данные!")


def change_contact(data_tuple):
    # Изменение существующей записи

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Данные уже существуют!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Запись изменена!\n")


def search_contact():
    search_data = exist_contact(0, input("Введите данные поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Некорректные данные!")


def exist_contact(rec_id, data):
    # Проверка записи в базе

    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
    # Проверка полученных данных

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "Фамилия Имя Отчество":
            if answer.isalpha():
                break
        if num == "Номер телефона":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Некорректные данные!\n"
                       f"Используйте только буквы"
                       f" алфавита, или максимум 11 цифр\n"
                       f"Введите {num}: ")
    return answer


def main_menu():
    # Основное меню

    play = True
    while play:
        read_records()
        answer = input("Телефонная книга:\n"
                       "1. Показать все записи\n"
                       "2. Добавить запись\n"
                       "3. Найти запись\n"
                       "4. Изменить запись\n"
                       "5. Удлить запись\n"
                       "6. Экспорт/Импорт\n"
                       "7. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                export_import_menu()
            case "7":
                play = False
            case _:
                print("Попробуйте ещё раз!\n")


def edit_menu():
    # Меню редактирования

    add_dict = {"1": "Фамилия", "2": "Имя", "3": "Отчество", "4": "Номер телефона"}

    show_all()
    record_id = input("Введите id записи: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. Фамилия\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. Номер телефона\n"
                           "5. Выход\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Данные не распознаны, повторите ввод.")
    else:
        print("Некорректные данные!")


def export_bd(name):
    # Сохранение данных в новый файл

    symbol = "\n"

    if not path.exists(name):
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def ipmort_bd(name):
    global file_base
    if path.exists(name):
        file_base = name
        read_records()


def export_import_menu():
    # Меню экспорта/импорта

    while True:
        print("\nМеню Экспорта/Импорта:")
        move = input("1. Импорт\n"
                     "2. Экспорт\n"
                     "3. Выход\n")

        match move:
            case "1":
                ipmort_bd(input("Введите название файла: "))
            case "2":
                export_bd(input("Введите название файла: "))
            case "3":
                return 0
            case _:
                print("Данные не распознаны, повторите ввод.")


main_menu()
