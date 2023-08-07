# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
# array_size = int(input("Введите кол-во эл-ов: "))
# a1 = int(input("Введите первый эл-т: "))
# diff = int(input("Введите диф: "))
# res = []
# for i in range(array_size):
#     # res2 = a1 + i * diff
#     res.append(a1 + i * diff)
# print(res)

# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
# from random import randint
# array = [randint(-10, 10) for i in range(int(input("Enter size of array: ")))]
# print(array)
# num_min = 5
# num_max = 15
# new_array = []
# for i in range(len(array)):
#     # if num_min < array[i] and num_max > array[i]:
#     if num_min < array[i] < num_max:
#         new_array.append(i)
# print(new_array)
