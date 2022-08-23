import unittest

from sampletest.square import square


class TestSquare(unittest.TestCase):
    def test_square(self):
        actual = square(2)
        expected = 4
        self.assertEqual(actual, expected)

    def test_square_with_array(self):
        actual = [square(i) for i in range(5)]
        expected = [0, 1, 4, 9, 16]
        self.assertListEqual(actual, expected)
