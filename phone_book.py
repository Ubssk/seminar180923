# Создать телефонный справочник с возможностью импорта и экспорта данных в формате
# .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def enter_first_name():
    return input("Введите имя абонента: ").title()

def enter_second_name():
    return input("Введите фамилию абонента: ").title()

def enter_family_name():
    return input("Введите отчество абонента: ").title()

def enter_phone_number():
    return input("Введите номер телефона: ")

def enter_address():
    return input("Введите адрес абонента: ").title()

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{name} {surname} {family}\n {number}\n {address}\n')

def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())

def search_line():
    print('Выберите вариант поиска: \n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index=int(input('Введите вариант: ')) -1
    searched=input('Введите поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        # print(file.read().split('\n\n'))
        data=file.read().split('\n\n')
        for item in data:
            new_item=item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end="\n\n")
        # file.seek(0)
        # print(file.readlines())
        # file_read=

def replace():
    print('Выберите что нужно изменить: \n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index=int(input('Введите вариант: ')) -1
    searched=input('Введите поисковые данные: ').title()
    replace_item=input('Введите измененные данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data=file.read().strip().split('\n\n')
    new_data=[]
    for item in data:
        new_item=item.replace('\n', ' ').split()
        if new_item[index]==searched:
            new_item[index]=replace_item
            new_data.append(f'\n{new_item[0]} {new_item[1]} {new_item[2]}\n {new_item[3]}\n {new_item[4]}\n')
        else:
            new_data.append(item)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(new_data))

def deletion(): 
    print('Выберите вариант удаления: \n' 
          '1. Имя\n' 
          '2. Фамилия\n' 
          '3. Отчество\n' 
          '4. Телефон\n' 
          '5. Адрес') 
    index = int(input('Введите вариант: ')) - 1 
    searched = input('Введите данные которые надо удалить: ').title() 
    with open('book.txt', 'r', encoding='utf-8') as file: 
        data = file.read().strip().split('\n\n') 
    new_data = [] 
    for item in data: 
        if searched in item: 
            new_item = item.replace('\n', ' ').split() 
            if new_item[index] == searched: 
                continue
            else: 
                new_data.append(item) 
        else:
            new_data.append(item)
    with open('book.txt', 'w', encoding='utf-8') as file: 
        file.write('\n\n'.join(new_data))

def interface():
    cmd=0
    while cmd != '6':
        print('Выберите варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск контакта\n'
            '4. Изменение контакта\n'
            '5. Удаление контакта\n'
            '6. Выход')
        cmd= input('Введите действие: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd= input('Введите действие: ')
        match cmd:
            case '1': 
                enter_data()
            case '2': 
                print_data()
            case '3': 
                search_line()
            case '4': 
                replace()
            case '5': 
                deletion()
            case '5': 
                print('Всего доброго!')
      
interface()