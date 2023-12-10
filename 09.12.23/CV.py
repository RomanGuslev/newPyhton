# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def set_param(c=20, s="-"):
#     print(s * c)
#
# set_param()
# set_param(7)
# set_param(5, "*")
# set_param(s="#")

#
# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current %2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name,  "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")


# ___________________________________________________________
# Изменяемые и неизменяемые объекты

#
# lt1 = (1, 2, 3)
# lt2 = (1, 2, 3)
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)
#
# n = 5
# m = 5
# print(n == m)
# print(n is m)
#
# n = (1, 2, 3)
# print(id(n))


# Кортеж

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = 5, 9, 7, 8
# print(type(a))
# # b = tuple()
# print (a)

# n = [1, 2, 3]
# b = tuple("Hello", "Python")
# print(type(b))
# print(b)
#
# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])
# print(a[1:3])

# from random import randint
# s = tuple(2 ** i for i in range(1, 13))
# print(s)


# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# # print(t3.count('l'))
# # print(t3.index('l', 4, -2))
# print(t3)
# for i in t3:
#     print(i, end=" ")
#
#


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # a = tpl.index(el)
#             # b = tpl.index(el, a + 1) + 1
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (10, 11, [1,2,3], [4,5,6],['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


first_name, year, married = get_user()
print(first_name, year, married)
