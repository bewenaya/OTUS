from itertools import count
from os import remove
from os.path import split

original_file = 'telephone_catalog.txt'

# Возвращает список с содержанием файла (построчно)
def open_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        content = file.readlines()
        result = []
        for row in content:
            result.append(row.strip().split(';'))
        return result

# Сохранить файл после изменения
def save_file_after_add(change):
    global original_file
    new_str = list_to_str(change)
    with open(original_file, 'a', encoding='UTF-8') as file:
        file.write(new_str)
        print('Данные успешно сохранены.')

# Показать все контакты
def show_all_contacts(file_name):
    result = open_file(file_name)
    contact = {}
    for id,item in enumerate(result, 1):
        contact[id] = {
            'Идентификатор': item[0],
            'Имя': item[1],
            'Телефон': item[2],
            'Комментарий': item[3]
        }
    for id, item in contact.items():
        print(f'\nКонтакт №{id}')
        for key, value in item.items():
            print(f'\t{key:<14} {value}')

# Создать новый контакт
def create_contact(file_name):
    result = open_file(file_name)
    max_id = 0
    for item in result:
        if max_id < int(item [0]):
            max_id = int(item[0])
        else:
            continue
    new_contact = []

    new_contact_id = max_id + 1
    new_contact_name = get_param('Введите имя нового контакта: ')
    new_contact_phone = get_param('Введите телефон нового контакта: ')
    new_contact_comment = get_param('Введите комментарий для нового контакта: ')

    new_contact.append(str(new_contact_id))
    new_contact.append(new_contact_name)
    new_contact.append(new_contact_phone)
    new_contact.append(new_contact_comment)

    save_file_after_add(new_contact)
    return (new_contact)

# Запросить значения параметра у пользователя
def get_param(text_input):
    param = ''
    while param == '':
        param = input(text_input)
        if not param:
            print('Параметр должен иметь значение!\n')
            continue
    return param

# Преобразование списка в строку
def list_to_str(my_list):
    string = (';'.join(my_list)) + '\n'
    return(string)

# Поиск значения
def search_contact(file_name):
    result = open_file(file_name)
    count = 0

    query = get_param('Введите запрос для поиска контакта: ')
    for item in result:
        search_string = list_to_str(item)
        if search_string.find(query) != -1:
            count += 1
            contact = {
                'Идентификатор': item[0],
                'Имя': item[1],
                'Телефон': item[2],
                'Комментарий': item[3]
            }
            for key, value in contact.items():
               print(f'\t{key:<14} {value}')
            print()
        else:
            continue
    if count == 0:
        print('Результаты не найдены.')

#Обновить строку из файла
def update_contact(file_name):
    result = open_file(file_name)
    query = str(get_param('Введите идентификатор контакта, который нужно изменить: '))
    i = 0
    count = 0
    while i < len(result):
        line = result[i]
        if line[0] == query:
            print('''Выберите значение, которое нужно изменить :
            1 - Изменить имя
            2 - Изменить телефон
            3 - Изменить комментарий
            4 - Выход
            ''')
            menu = input('Введите пункт меню >>> ')
            if menu == '1':
                new_name = get_param('Введите новое имя контакта: ')
                line[1] = new_name
                save_file_after_upd(result)
                break
            elif menu == '2':
                new_phone = get_param('Введите новый номер телефона контакта: ')
                line[2] = new_phone
                save_file_after_upd(result)
                break
            elif menu == '3':
                new_comment = get_param('Введите новый номер комментарий контакта: ')
                line[3] = new_comment
                save_file_after_upd(result)
                break
            else:
                raise SystemExit
        else:
            count += 1
        i += 1
    if count == len(result):
        print('Значение не найдено.')

#Сохранить файл после изменения строки
def save_file_after_upd(change):
    global original_file
    with open(original_file, 'w', encoding='UTF-8') as file:
        for line in change:
            new_str = list_to_str(line)
            file.write(new_str)
        print('Данные успешно сохранены.')

# Удалить строку из файла
def delete_contact(file_name):
    result = open_file(file_name)
    query = str(get_param('Введите идентификатор контакта, который нужно удалить: '))
    i = 0
    count = 0
    while i < len(result):
        line = result[i]
        if line[0] == query:
            result.remove(line)
            save_file_after_del(result)
            break
        else:
            count += 1
        i += 1
    if count == len(result):
        print('Значение не найдено.')

# Сохранить файл после удаления
def save_file_after_del(change):
    global original_file
    with open(original_file, 'w', encoding='UTF-8') as file:
        for line in change:
            new_str = list_to_str(line)
            file.write(new_str)
        print('Данные успешно сохранены.')

print('''Выберите пункт меню :
1 - Показать все контакты
2 - Создать контакт
3 - Найти контакт
4 - Изменить контакт
5 - Удалить контакт
6 - Выход
''')

while True:
    menu = input('Введите пункт меню >>> ')
    if menu == '1':
        show_all_contacts(original_file)

    elif menu == '2':
        create_contact(original_file)

    elif menu == '3':
        search_contact(original_file)

    elif menu == '4':
        update_contact(original_file)

    elif menu == '5':
        delete_contact(original_file)

    elif menu == '6':
        raise SystemExit

    else:
        print('Выбран несуществующий пункт меню')