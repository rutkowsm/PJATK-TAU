import unittest
from TAU1 import main as main


class TestMain(unittest.TestCase):

    def test_sum_equals(self):
        self.assertEqual(main.sum(5, 5), 10)

    def test_sum_notequals(self):
        self.assertNotEqual(main.sum(15, 25), 159)

    def test_if_true(self):
        self.assertTrue(main.is_true(5, 5))

    def test_if_false(self):
        self.assertFalse(main.is_true(10, 9))

    def test_if_greater(self):
        self.assertGreater(main.multiplication(2, 2), 3)

    def test_if_less(self):
        self.assertLess(main.multiplication(2, 2), 10)

    def test_if_list_equal(self):
        self.assertListEqual(main.example_list(['yes', 'no']), main.example_list(['yes', 'no']))

    def test_if_item_in_list(self):
        self.assertIn(main.example_string('yes'), 'yes')

    def test_if_item_not_in_list(self):
        self.assertNotIn(main.example_string('yes'), 'no')

    def test_if_is_not_none(self):
        self.assertIsNotNone(main.multiplication(2, 2))

if __name__ == '__main__':
    unittest.main()