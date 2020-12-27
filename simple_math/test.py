import unittest

from .func import add


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(42, add(40, 2))


if __name__ == '__main__':
    unittest.main()
