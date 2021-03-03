import unittest
from .my_pow import my_pow
from .half_adder import add


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for x in range(0, -5, -1):
            for y in range(-2, 100):
                self.assertEqual(pow(x, y), my_pow(x, y))

    def test_half_add(self):
        """
        Test Add operation without using add operator
        """
        for x in range(100):
            for y in range(100):
                self.assertEqual(x + y, add(x, y))


if __name__ == '__main__':
    unittest.main()
