# number = (6 + 4) * (5 ** 2 + 7)
# # print(number)
#
# num = 10
# num += 5  #  num = num + 5
# print (num)  #  15
#
# num -= 3  #  num = num -3
# print(num)

#
# num = 4321
# print("Исходное число:", num)
# a = num % 10
#
# num //= 10
#
# b = num % 10
# num //= 10
# c = num % 10
# num //= 10
# d = num % 10
# print(a * 100 + b * 100 + c * 10 + d)

# num = 4321
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
#
# print(res)

# num1 = "2"
# num2 = 3
# # res = num1+str(num2) #23
# res = int(num1) + num2
# print(res)


# print(int(3.8))
# print(round(3.891, 2))
# print(type(round(3.891, 2)))

#
# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", str(age), "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="&&&&", end=" ")
# print("Я учу Python")


# name = input("Введите имя: ")
# print(name)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# res = num ** int(power)
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1+5
# print(b2 + 5)  # 0+5

# False => "", 0, False, None
#
# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10-7)
# print(8 > 5)
# print(8 > 5)
# print(9 <= 9)
# print(9 >= 9)
# print("Привет" > "ПРИВЕТ")

#
# print(2 < 4 < 9)  # 2 < 4 < 9 => True && True
# print(2 * 5 > 7 >= 4 + 3)  # True && True
# print(3 * 3 <= 7 >= 2) # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 false


# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)


# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)
#
#
# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)


# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)
#

#
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен.")
# else:
#     print("Доступ на сайт запрещен.")

#
# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")
#
#

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью. сторону: "))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')


# day = int(input("Введите день недели цифрой: "))
# if 1<= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня нет")
