n = int(input("Введите количество символов: "))
symbol = input("Тип символа: ")
orient = int(input("0 - Горизонтальная\n1 - Вертикальная\nориентация линии: "))
i = 0
while i < n:
    if orient == 0:
        print(symbol, end=" ")
    if orient == 1:
        print(symbol)
    i += 1