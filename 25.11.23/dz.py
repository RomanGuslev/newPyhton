numbers = [int(input('-> ')) for _ in range(int(input('Введите количество элементов списка: ')))]
sum_of_numbers = sum(numbers)
count_of_zero = numbers.count(0)
count_of_numbers = len(numbers) - count_of_zero
average = sum_of_numbers / count_of_numbers
print('Средне арифметическое: ', average)