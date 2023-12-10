# for i in range (3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")


# _____________________________________________
# вложенный цикл for

# for i in range(3):
#     print("+++ i =", i)
#     for j in range(2):
#         print("----- j+", j)
# _________________________________________________
# _________________________________________________
# задача вывести на экран прямоугольник , ширину и высоту задает пользователь

# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()
# _____________________
# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h -1 or j == 0 or j == w -1 :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# ______________________________________________
# ______________________________________________


# Списки for
# nums = [letter * 2 for letter in "Banana"]
# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)0

# Списки (list)
# nums = [8, 3, 99, 4, 1, "one"]
# print(nums)
# # print(type(nums))
# #
# #
# # print(nums[0])
# # # print(nums[6]) #index error
# # print(nums[-1])
# # nums[-1] = 256
# # print(nums)
# # nums[3] += 100
# # print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)
#
# s = []
# print(s)
#
# b = list("Hello")
# print(b)
# print(b[0])

# print(range(6))
# n = list(range(6))
# print(n)
# print(list(range(2, 10)))
# print(list(range(2, 10, 2)))

#  [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)
# b = [i for i in range(5)]
# print(b)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)


# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)
# ___________________________________________________________________
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# СОКРАЩЕННЫЙ ВАРИАНТ:

# a = [input("->") for i in range(int(input("n=")))]
# print(a)
# _________________________________________________________________

# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)

#
# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i] +2, end=" ")
# print()
#
# for i in a:
#     print(i +2, end=" ")

# _______________________________________________

# В списке на 20 элементов посчитать кол-во четных и найти сумму не четных :

# n = list(range(21, 41))
# print(n)
# s = k = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         k += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("sum нечетных эл-ов: ", s)
# print("count четных эл-ов: ", k)
# ________________________
# ________________________
# ДАн список чисел . выведите все элементы списка которые больше предыдущего:

# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")

# a = [int(input("->")) for i in range(int(input("n=")))]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         print(a[i+1])

# from random import randint
#
# a = randint(1, 100)
# b = int(input("Угадайте целое число от 1 до 100:"))
# while b != a:
#     b = int(input("Повторите попытку:"))
#     if b < a:
#         print("Ваше число меньше, чем задумал компьютер")
#     elif b > a:
#         print("Ваше число больше, чем задумал компьютер")
#     else:
#         print("Вы угадали")
# print(b)
# print(a)
