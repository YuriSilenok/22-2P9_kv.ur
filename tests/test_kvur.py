"""Автотест для нахожденеия квадратного уравнения
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
