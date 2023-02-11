Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

m = int(input('Кол-во элементов первого множества: '))
lst = []
i = 0
while i < m:
    string = "Введите элемент №" + str(i + 1) + ": "
    lst.append(input(string))
    i += 1
print(lst)

n = int(input('Кол-во элементов второго множества: '))
lst2 = []
j = 0
while j < n:
    string2 = "Введите элемент №" + str(j + 1) + ": "
    lst2.append(input(string2))
    j += 1
print(lst)
print(lst2)
lst3 = []

for a in lst:
    for b in lst2:
        if a == b:
            lst3.append(a)
            break
lst3.sort()
print(lst3)



Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система
автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения
максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input( 'Введите кол-во кустов: '))
lst = [int(x) for x in input( 'Введите количество ягод на кустах: ').split()]
n = len(lst)
lst = lst + lst[:2]
sum = 0
for i in range(n):
    sum = max(sum, lst[i] + lst[i+1] + lst[i+2])
print(sum)
