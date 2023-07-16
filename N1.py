# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

# n = 123
# first_index = n // 100
# second_index = n // 10 % 10
# third_index = n % 10
# res = first_index + second_index + third_index
# print(res)

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

# n = 60
# petya = n // 6
# sereja = petya
# katya = (petya + sereja) * 2
# print(petya, katya, sereja)

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# Пример:
# n = 385916 -> yes
# n = 123456 -> no

# num = int(input("Введите число: "))
# num = 385916
# first = num // 100000
# second = num // 10000 % 10
# third = num // 1000 % 10
# fourth = num // 100 % 10
# fifth = num // 10 % 10
# sixth = num % 10
# if first + second + third == fourth + fifth + sixth:
#     print("yes")
# else:
#     print("no")

# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

# a = 3
# b = 2
# c = 4
# if c % a == 0 or c % b == 0:
#     print("yes")
# else:
#     print("no")