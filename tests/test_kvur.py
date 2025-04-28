"""Автотест для нахожденеия корней квадратного уравнения"""


import unittest
from logic import kv_ur


class Testkvur(unittest.TestCase):
    """Автотест для нахожденеия корней квадратного уравнения"""
    def test_lessthanzero(self):
        """Автотест для нахожденеия корней квадратного уравнения"""
        result = kv_ur(9, -6, 2)
        responce = ('Квадратное уравнение. Дискриминант меньше 0. '
                    'Уравнение не имеет корней', 'корней нет')
        self.assertEqual(result[0], responce[0])
        self.assertEqual(result[1], responce[1])
