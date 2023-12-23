# # множество (set)
#
# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))

# c= ["red", "blue", "green", "red"]
# a = set(c)
# print(a, type(a))
#
#
# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas if x % 2 == 0}
# print(s)


# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

#
#
# t = {"red", "green", "blue"}
# # print("green" in t)
# for i in t:
#     print(i)
#
# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2 ']
# a = ['A' +i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)
#
# a = {'Tom', 'Bob', 'Alice'}
# print(a)
# a.add('Ann')
# print(a)
# a.remove("Ann")
# print(a)
# user = "Tom"
# if user in a:
#     a.remove(user)
# print(a)
# a.discard("Ann1")
# print(a)
# n = a.pop()
# print(a)
# print(n)
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a | b
# a |= b
# c = a & b
# a &= b
# c = a - b
# a -= b
# c = a ^ b
# a ^= b
# print(c)
# print(a)
# print(a)


s1 = {1, 2}
s2 = {3}
s3 = {4, 5}
s4 = {3, 2, 6}
s5 = {6}
s6 = {7, 8}
s7 = {9, 8}

# s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# count = len (s)
# print("cont:", count)
# print("Min:", min(s))
# print("Max:", max(s))
# print("Sum:", sum(s))


# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")


# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# one_hobby = drawing ^ music
# print("Один кружок:", one_hobby)
# both_hobbies = drawing & music
# print("Оба кружка:", both_hobbies)


# Тип Frozenset

# s = frozenset([1, 2, 3, 4, 5])
# print(s, type(s))
#
# a = frozenset({"hello", "world"})
# print(a)
#


# a = [8, 9, 7, 4, 5, 8, 7, 9, 4, 6, 5, 1, 2, 3, 5]
# print(a)
# b = set(a)
# print(b)
# a = list(b)
# print(a)
# a = tuple(b)
# print(a)