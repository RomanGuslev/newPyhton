# d = {'a': 1, 'c': 3, 'b': 2}
# # d1 = {'r': 7, 'q': 40}
# # d.update(d1)
# #
# # # d2 = {'a': 20, 'b': 9}
# # d2 = [('a', 20), ('b', 9)]
# # d.update(d2)
# # print(d)
#
# #
# # x = {
# #     'a' : 1,
# #     'b' : 2
# # }
# #
# # y = {
# #     'b' : 3,
# #     'c' : 4
# # }
# # # new_dict = x.copy()
# # # new_dict.update(y)
# # new_dict = x | y
# # print(new_dict)
#
# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t",y, ": ", a[x][y], sep="")

# sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#          "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#          "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#          "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t",y, ": ", sales[x][y], sep="")
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])
# d =  {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# new_d = {key: value for key, value in d.items()}
# print(new_d)
# d = {"N": 1, "S": 2, "E": 3, "W": 4}
#
# value = list(d.items())
# print(value)
#
# value = list(d)
# print(value)

# a = ["one", 1,2,3, "two", 10,20, "three", 15, 36, 60, "four", -20]
# d = dict() #{}
# current_key = ""
# for item in a:
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
# print(d)

# d = dict(zip([1,2,3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# c = tuple(zip(a, b))
# print(c)

# d_one = {'name': "Igor", "last_name": "Petrov", "job": "Consultant"}
# d_two = {'name': "Irina", "last_name": "Irisova", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#
# d = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*d)
# print(a)
# print(b)

# a = ('two', 'one', 'three')
# b = (3, 2, 1)
# d = list(zip(a, b))
# print(d)
# d.sort()
# print(d)
# print(dict(d))
# # s = sorted(d.items())
# # print(s)
#
# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two}) #{'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
# for k, v in {**two, **one}.items():
#     print(k, "->", v)
#
# data = ["red", "green", "blue"]
# num = 1
# for val in data:
#     print(num, ")", val, sep="")
#     num +=1
# print()
# for num, val in enumerate(data, start=1):
#     print(num, ")", val, sep="")