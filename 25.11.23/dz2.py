numbers = [int(input('-> ')) for _ in range(int(input('Введите количество элементов: ')))]
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i], end=' ')