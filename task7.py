def cyclic_shift(word, n):

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    n = n % len(word)
    return word[-n:] + word[:-n]
import unittest
from 123123 import cyclic_shift

class TestCyclicShift(unittest.TestCase):
    def test_positive_shift(self):
        self.assertEqual(cyclic_shift("hello", 2), "llohe")

    def test_negative_shift(self):
        self.assertEqual(cyclic_shift("hello", -2), "lohel")

    def test_shift_by_length(self):
        self.assertEqual(cyclic_shift("hello", 5), "hello")

    def test_empty_string(self):
        self.assertEqual(cyclic_shift("", 3), "")

    def test_non_integer_shift(self):
        with self.assertRaises(ValueError):
            cyclic_shift("hello", 3.14)

    def test_zero_shift(self):
        with self.assertRaises(ValueError):
            cyclic_shift("hello", 0)

    def test_negative_shift_value(self):
        with self.assertRaises(ValueError):
            cyclic_shift("hello", -1)
    if __name__ == '__main__':
        unittest.main()