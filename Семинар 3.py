# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X
#
# from random import randint
#
# x = int(input('Введите размерность массива: '))
# n = int(input('Введите число которое будем искать: '))
#
# lst = [randint(-10, 10) for _ in range(x)]
# count = lst.count(n)
# print(lst)
# print(count)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X.

# from random import randint
#
# x = int(input('Введите размерность массива: '))
# n = int(input('Введите число которое будем искать: '))
#
# lst = [randint(-10, 10) for _ in range(x)]
#
# def nearest_n(lst, n):
#
#     found = lst[0]
#     for item in lst:
#         if abs(item - n) < abs(found - n):
#             found = item
#     return found
#
# print(f'Ближайшее число к {n} в списке {lst} является {nearest_n(lst, n)}')

# Задача 20: Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# def fun(x):
# 	for key in dct:
# 		if x in key:
# 			return dct.get(key)
#
# word = input('Введите слово:')
#
# dct = {
# 	'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3,
# 	'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10, 'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3,
# 	'ЙЫ': 4, 'ЖЗЧЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10
# }
#
# print(sum(map(fun, word.upper())))

