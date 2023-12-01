import unittest
from TAU1.main import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    def test_add_is_not_none(self):
        self.assertIsNotNone(self.calculator.add(2, 2))

    def test_subtract_not_equal(self):
        self.assertNotEqual(self.calculator.subtract(2, 2), 1)

    def test_multiply_greater_than(self):
        self.assertGreater(self.calculator.multiply(3, 3), 8)

    def test_divide_less_than(self):
        self.assertLess(self.calculator.divide(1, 2), 1)

    def test_multiply_is_instance(self):
        self.assertIsInstance(self.calculator.multiply(2, 2), int)

if __name__ == '__main__':
    unittest.main()
