def show_menu():
    print('''Здравствуйте! Для начала работы со справочником выберите действие, которое требуется выполнить:
          1. Напечатать весь справочник.
          2. Искать по имени.
          3. Искать по номеру телефона.
          4. Добавить нового абонента.
          5. Сохранить справочник в текстовый файл.
          6. Изменить данные абонента.
          7. Удалить абонента.
          8. Выйти из программы''')
    try:
        choice = int(input('Введите число от 1 до 8, обозначающее пункт меню: '))
        return choice
    except Exception:
        print('Некорректный ввод данных!')

def print_result(data):
    for unit in data:
        print(f'''{data.index(unit) + 1}. {unit['Фамилия']} {unit['Имя']}. Телефон: {unit['Телефон']}. ({unit['Описание']})''')

def get_search_name():
    search_name = input('Введите имя или фамилию абонента: ')
    return search_name.lower()

def find_by_name(data, search_name):
    result = []
    for unit in data:
        for key, value in unit.items():
            if (key == 'Имя' or key == 'Фамилия') and search_name in value.lower():
                if unit not in result:
                    result.append(unit)
    return result

def get_search_number():
    search_number = input('Введите номер абонента: ')
    return search_number

def find_by_number(data, search_number):
    result = []
    for unit in data:
        for key, value in unit.items():
            if key == 'Телефон' and str(search_number) in str(value):
                result.append(unit)
    return result

def get_new_user():
    while True:
        new_user = {}
        print('Введите данные нового абонента:')
        new_user['Фамилия'] = input('Фамилия: ')
        new_user['Имя'] = input('Имя: ')
        new_user['Телефон'] = input('Номер телефона: ')
        new_user['Описание'] = input('Описание: ')
        if '' in new_user.values():
            print('Вы заполнили не все данные!')
        else:
            return new_user

def add_user(data, new_user):
    data.append(new_user)

def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for unit in data:
           file.write(','.join(list(unit.values())) + '\n')

def get_file_name():
    while True:
        file_name = input('Введите название нового файла: ')
        if file_name:
            return file_name
        else:
            print('Некорректный ввод данных!')

def write_txt(filename, data):
    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
        for unit in data:
            file.write(','.join(list(unit.values())) + '\n')

def read_csv(filename):
    data = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def choice_of_method():
    print('''Выберите способ поиска абонента:
          1. По имени.
          2. По номеру телефона.''')
    while True:
        try:
            choice = int(input('Введите число, обозначающее пункт меню: '))
            if choice == 1:
                arg = get_search_name()
            elif choice == 2:
                arg = get_search_number()
            return [[find_by_name, arg], [find_by_number, arg]][choice - 1]
        except Exception:
            print('Некорректный ввод данных!')

def choice_of_user(data):
    print_result(data)
    if len(data) > 1:
        while True:
            try:
                chosen_user = int(input('Выберите необходимого абонента, введя соответствующее число: '))
                return data[chosen_user - 1]
            except Exception:
                print('Некорректный ввод данных!')
    else:
        return data[0]

def choice_of_field():
    while True:
        try:
            print('''Выберите поле, которое необходимо изменить:
                  1. Фамилия.
                  2. Имя.
                  3. Телефон.
                  4. Описание.''')
            field = ['Фамилия', 'Имя', 'Телефон', 'Описание'][int(input('Введите число, обозначающее поле: ')) - 1]
            return field
        except Exception:
            print('Некорректный ввод данных!')

def change_user(data, user, field):
    new_value = input('Введите новое значение: ')
    data[data.index(user)][field] = new_value

def del_user(data, user):
    data.remove(user)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    while choice != 8:
        if choice == 1:
            print_result(phone_book)
            input('Для продолжения нажмите Enter...')
        elif choice == 2:
            name = get_search_name()
            result = find_by_name(phone_book, name)
            print_result(result) if result else print('Данные не найдены.', end=' ')
            input('Для продолжения нажмите Enter...')
        elif choice == 3:
            number = get_search_number()
            result = find_by_number(phone_book, number)
            print_result(result) if result else print('Данные не найдены.', end=' ')
            input('Для продолжения нажмите Enter...')
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
            input('Для продолжения нажмите Enter...')
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
            input('Для продолжения нажмите Enter...')
        elif choice == 6:
            func, arg = choice_of_method()
            result = func(phone_book, arg)
            if result:
                chosen_user = choice_of_user(result)
                chosen_field = choice_of_field()
                change_user(phone_book, chosen_user, chosen_field)
                write_csv('phonebook.csv', phone_book)
            else:
                print('Данные не найдены.', end=' ')
            input('Для продолжения нажмите Enter...')
        elif choice == 7:
            func, arg = choice_of_method()
            result = func(phone_book, arg)
            if result:
                chosen_user = choice_of_user(result)
                del_user(phone_book, chosen_user)
                write_csv('phonebook.csv', phone_book)
            else:
                print('Данные не найдены.', end=' ')
            input('Для продолжения нажмите Enter...')

        choice = show_menu()


work_with_phonebook()
