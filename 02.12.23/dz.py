from random import randint, choice
list_len = int(input('Ведите длину списка: '))
lst = []
num_list = [i for i in range(list_len)]
while len(lst) != list_len:
    element = choice(num_list)
    if element not in lst:
        lst.append(element)
print(lst)