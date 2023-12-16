from math import pi


def get_area_of_rectangle(base: float = None, height: float = None) -> float:
    if base is None:
        base = float(input('Введите длинну прямоугольника: '))
    if height is None:
        height = float(input('Введите высоту прямоугольника: '))
    return base * height


def get_area_of_triangle() -> float:
    base = float(input('Введите основание треугольника: '))
    height = float(input('Введите высоту треугольника: '))
    return get_area_of_rectangle(base=base, height=height) / 2


def get_area_of_circle() -> float:
    radius = float(input('Введите радиус окружности: '))
    return round(pi, 2) * (radius ** 2)


def ask_choice() -> str | None:
    choice = int(input('Выберите фигуру: '
                       '\n1-прямоугольник, '
                       '\n2-треугольник, '
                       '\n3-круг, '
                       '\n0 -выход: '))

    match choice:
        case 0:
            return
        case 1:
            print('Площадь прямоугольника:', "{:.2f}".format(get_area_of_rectangle()))
        case 2:
            print('Площадь треугольника:', '%.2f' % get_area_of_triangle())
        case 3:
            print('Площадь окружности:', round(get_area_of_circle(), 2))
        case _:
            print('Вы ввели не допустимое значение. Проверьте правильность ввода и повторите попытку.')
            ask_choice()


ask_choice()
