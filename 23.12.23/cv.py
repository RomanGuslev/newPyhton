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

sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
         "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
         "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
         "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
for x in sales:
    print(x)
    for y in sales[x]:
        print("\t",y, ": ", sales[x][y], sep="")
person = input("Имя: ")
region = input("Регион: ")
print(sales[person][region])
new_data = int(input("Новое значение: "))
sales[person][region] = new_data
print(sales[person])