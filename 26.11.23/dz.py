numbers = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for number in numbers:
    if numbers.count(number) > 1:
        continue
    else:
        print(number, end=' ')