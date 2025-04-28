"""Модуль для решения квадратного уравнения."""


def kv_ur(a, b, c):
    """Решает квадратное или линейное уравнение."""
    if a == 0:
        if b == 0:
            if c == 0:
                return "Прямая совпадает с осью Ox", "R"
            return "Прямая параллельна оси Ox", "Корней нет"
        x = -c / b
        return "Линейное уравнение, один корень", x

    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b - disc ** 0.5) / (2 * a)
        x2 = (-b + disc ** 0.5) / (2 * a)
        return "Два корня", x1, x2
    if disc == 0:
        x = -b / (2 * a)
        return "Один корень", x
    return "Комплексные корни", "Нет вещественных решений"


if __name__ == "__main__":
    try:
        A = float(input("Введите a: "))
        B = float(input("Введите b: "))
        C = float(input("Введите c: "))
        res = kv_ur(A, B, C)
        print(res)
    except ValueError:
        print("Ошибка, введите корректные числовые значения!!!")
