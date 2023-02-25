from reading_a_file import*
print_help()
try:
    command = int(input('Выберите команду: '))
    while command != 0:
        if command == 1:
            list_sprav()
        elif command == 2:
            save()
        elif command == 3:
            search = input('Введите данные: ')
            data_search(search)
        elif command == 4:
            print_help()
        elif command == 0:
            break
        else:
            print("Такой команды нет в списке!")
        command = int(input('Выберите команду: '))
except ValueError:
    print('Введены не корректные данные!')