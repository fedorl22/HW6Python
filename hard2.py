# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать 
# случайным образом элементы массива, причем чтобы каждый гарантированно и только один раз переместился 
# на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить 
# не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

# from random import randint
# m = int(input('Введите количество столбцов'))
# n = int(input('Введите количество строк'))
# # n, m = 3, 4
# a = [[randint(1, 29) for j in range(m)] for i in range(n)]
# for i in range(0, n):
#     for j in range(0, m):
#         print(a[i][j], end=' ')
#     print()
# lstn = list(range(0, n))
# lstm = list(range(0, m))
# sn = set(lstn)
# sm = set(lstm)
# count = 0
# for i in range(0, n):
#     if i in sn:
#         for j in range(0, m):
#             if j in sm:
#                 sn.discard(i)
#                 sm.discard(j)
#                 k = randint(0, n-1)
#                 l = randint(0, m-1)
#                 print(sn)
#                 print(sm)
#                 print(k)
#                 print(l)
#                 if k in sn and l in sm:
#                     temp =a[i][j]
#                     a[i][j] = a[k][l]
#                     a[k][l] = temp
#                     count+=1
#                     sn.discard(k)
#                     sm.discard(l)
# print(a)
# print(count)
