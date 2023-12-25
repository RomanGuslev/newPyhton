
VOWELS = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ё'}

string = input('Введите строку: ')

count = 0
for letter in string:
    if letter.lower() in VOWELS:
        count += 1

print('Количество гласных равно:', count)

