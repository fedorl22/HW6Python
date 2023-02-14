# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать 
# элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint
m = int(input('Введите количество столбцов'))
n = int(input('Введите количество строк'))
mas = [[randint(1, 9) for j in range(m)] for i in range(n)]
for i in range(0, n):
    for j in range(0, m):
        print(mas[i][j], end=' ')
    print()
mas2 = []
for i in range(0, n):
    for j in range(0, m):
        mas2.append(mas[i][j])
mas=sorted(mas2)
# print(mas)
print()
for i in range(0, n):
    for j in range(i* (m), i*(m)+m):
        print(mas[j], end=' ')
    print()