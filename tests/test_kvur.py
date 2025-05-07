"""Автотест для нахожденеия квадратного уравнения\
с отрицательным дискриминантом"""


import unittest
from logic import kv_ur


class Testkvur(unittest.TestCase):
    """Автотест для нахожденеия квадратного уравнения
    с отрицательным дискриминантом"""
    def test_lessthanzero(self):
        """Автотест для нахожденеия квадратного уравнения
        с отрицательным дискриминантом"""
        responce = ('Квадратное уравнение. Дискриминант меньше 0. '
                    'Уравнение не имеет корней', 'Корней нет')
        result = kv_ur(9, -6, 2)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], responce[0])
        self.assertEqual(result[1], -36)
        self.assertEqual(result[2], responce[1])

    def test_zero(self):
        """Автотест для написания квадратного уравнения
        с дискриминантом равным 0"""

        result = kv_ur(2, 4, 2)
        self.assertEqual(len(result), 3)
        self.assertEqual(
            result[0],
            'Квадратное уравнение. Дискриминант равен 0. '
            'Уравнение имеет один корень.'
        )
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], -1)

    def test_greaterthanzero(self):
        """Автотест для нахождения квадратного уравнения
        с положительным дискриминантом"""
        responce = ('Квадратное уравнение. Дискриминант больше 0. '
                    'Уравнение имеет два корня.')
        result = kv_ur(1, -3, 2)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], responce[0])
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 1)
        self.assertEqual(result[3], 2)
