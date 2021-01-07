import unittest


class StringTestCase(unittest.TestCase):

    def test_rsplit(self):
        test_line = "Jade Jade 42 M"
        x0 = test_line.split()
        x1 = test_line.rsplit(sep=" ", maxsplit=1)
        x2 = test_line.rsplit(sep=" ", maxsplit=2)
        x3 = test_line.rsplit(sep=" ", maxsplit=3)
        self.assertEqual(4, len(x0))
        # the parameter `maxsplit` means the maximum possible separator that could be accepted.

        # maxsplit == 1
        self.assertEqual(2, len(x1))
        self.assertEqual("Jade Jade 42", x1[0])
        self.assertEqual("M", x1[1])

        # maxsplit == 2
        self.assertEqual(3, len(x2))
        self.assertEqual("Jade Jade", x2[0])
        self.assertEqual("42", x2[1])
        self.assertEqual("M", x2[-1])

        # maxsplit == 3
        self.assertEqual(x0, x3)


if __name__ == '__main__':
    unittest.main()
