from random import randint

a = randint(1, 100)
b = int(input("Угадайте целое число от 1 до 100:"))
while b != a:
    b = int(input("Повторите попытку:"))
    if b < a:
        print("Ваше число меньше, чем задумал компьютер")
    elif b > a:
        print("Ваше число больше, чем задумал компьютер")
    else:
        print("Вы угадали")
print(b)
print(a)
