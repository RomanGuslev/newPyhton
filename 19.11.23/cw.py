#  Проверка введенного числа на четность
# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
#
#
#  -----------------------------------------------------------------
#
#
# i = 0
# while i < 10:
#     if 1 == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")
#  --------------------------------------------------------------------
# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1
#  ---------------------------------------------------------------
# while True:
#     n =  int(input("Введите положительное число: "))
#     if n < 0:
#         break
# --------------------------------------------------------------------------
#
#
# # Произведение всех введенных чисел, пока не ввести 0
# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print(res)
# #
# #----------------------------------------------------------------------------
#
#
# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)
# #
# #----------------------------------------------------------------------------
# #
# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1
# #
# #----------------------------------------------------------------------------
# # Вывод таблицы умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1
# --------------------------------------------------------------------------------
# Прямоугольник из символов ^
# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^",end="")
#         j += 1
#     print()
#     i += 1
# --------------------------------------------------------------------------------


# # ВАРИАНТ 1:
# i = 0
# while i < 5:
#     j = 0
#     while j < 15:
#         if i % 2 == 0:
#             print("+",end="")
#         else:
#             print("-",end="")
#         j += 1
#     print()
#     i += 1
#

# i = 0
# while i < 5:
#     j = 16
#     # while j < 16:
#     #     if i % 2 == 0:
#     #         print("+",end="")
#     #     else:
#     #         5print("-",end="")
#     #     j += 1
#     if j % 2 == 0:
#         print("+" * 16)
#     else:
#         print("-" * 16)
#         j += 1
#     i += 1
# --------------------------------------------------------------------------------
#########  Звездочки
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
#  ---------------------------------------------------------------

# for element in collection:
#   print (element)

# for i in "Hello", "world", "!":
#     print(i)

# ________________________
# for element in range:
#   print (element)
# print(range(5))
# range (start. stop. step)


# for i in range(1, 9):
#     print(i, end=" ")
# print()
#
# i = 9
#
# while i <9
#     print(i, end="  ")
#     i -= 2
# ------------------------------------------
#  вывести делителя числа
#
# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")
#
# _-----------------------------------------------
# for i in range(1, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')
# ________________________________________________
# ДЗ: