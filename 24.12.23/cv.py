# def func(args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))

# _________________________________________________
# def summa(*params):
#     res = 0
#     for i in params:
#         res +=i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))
# _________________________________________________

# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))
# _____________________________________________________

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 5, 6, 7))
# __________________________________________________
# def print_score(student, *scores):
#     print("Student_name:", student)
#     for score in scores:
#         print(score)
#
#
# print_score("Irina", 5,4,3,2,5)
# print_score("Igor", 5,4,3,2,5)
# print_score("Lev")
# ________________________________________-
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d=9))
# ___________________________________________
# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name="Irina", surname="Reznikova", age=22)
# intro(name="Igor", surname="Berukov",email='igor@mail.ru', age=22, phone="+79999999")
# __________________________________________________________
# def db(**kwargs):
#     my_dict.update(kwargs)
#     # print("Внутри функции:", id(my_dict))
#
# my_dict = {"one": "first"}
# # print(id(my_dict))
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31,weight=61, eyes_color='grey')
# print(my_dict)
# _________________________________________________________
# def func(a, b, *args,  **kwargs):
#     return a, b, args, kwargs
#
#
# print(func(5, 9, 7, 8, 4, 3, 2, 1))
# ______________________________________________________

#
# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# ___________________________________________#

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func()
# ______________________________________________

# def add_five(a):
#     x = 2
#
#     def add_som():
#         print("x =", x)
#         return a + x
#
#
# print(add_five(5))
# add_some()
# ____________________________________________________
# sum = 5
#
# lst = [9, 5, 8, 7, 6]
# print(sum(lst))
# ____________________________________________________
# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t0)
