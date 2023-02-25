import json
def list_sprav():
    with open('Spravochnik.json', 'r', encoding='utf-8') as file:
        text = json.load(file)
        for i in text:
            print(i, end = ' ')
        print()
import json
def save():
    array = []
    user = input('Введите ФИО и номер телефона: ')
    with open('Spravochnik.json', 'w', encoding = 'utf-8') as file:
        file.write(json.dumps(user, ensure_ascii=False))
        print('Данные успешно добавлены!')

def print_help():
    print(''' 
    0 - Выход
    1 - Показать справочник
    2 - Сохранить данные
    3 - Поиск записи
    4 - Помощь''')
def data_search(y):
    with open ('Spravochnik.json', 'r', encoding='utf-8') as file:
        score = 0
        while True:
            x = file.readline()
            if y in x:
                score += 1
                print(x)

            elif x =='':
                if score > 0:
                    break
                else:
                    print('Таких данных нет в списке!')
                    break
