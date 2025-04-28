"""вычисление квадратного корня"""
import cmath


def kv_ur(a, b, c):
    """Функиця, которая возвращает кортеж"""
    d = b**2 - 4 * a * c

    if d < 0:
        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
        count_k = "Дискриминант меньше нуля, уравнение имеет комплексные корни"
        return count_k, x1, x2

    return "Нет комплексных корней", None, None
