import unittest


class MathTestCase(unittest.TestCase):
    """
    Test with builtin function abs().
    """
    def test_abs(self):
        self.assertEqual(1, abs(-1))
        self.assertEqual(1, abs(1))
        self.assertEqual(0.5, abs(-0.5))
        self.assertEqual(0.5, abs(0.5))

    """
    Test some simple functions in `cmath` module.
    """
    def test_complex_abs(self):
        # Literal complex number
        self.assertEqual(5, abs(3+4j))

        # use builtin constructor complex()
        self.assertEqual(5, abs(complex(3.0, 4)))

    def test_polar_covert(self):
        import cmath
        z0 = 1.0 + 0.0j
        # Convert the complex number z0 into polar coordinate
        polar = cmath.polar(z0)

        self.assertAlmostEqual(1.0, polar[0])
        self.assertAlmostEqual(0.0, polar[1])

        # Convert the polar coordinate back to the complex number
        z = cmath.rect(*polar)
        self.assertAlmostEqual(z0.real, z.real)
        self.assertAlmostEqual(z0.imag, z.imag)


class BasicTypeTestCase(unittest.TestCase):
    """
    Test function with the basic primitive types and the conversion.
    """
    def test_bin_func(self):
        x = 42
        self.assertEqual('0b101010', bin(x))
        self.assertEqual(x, int(bin(x), 2))

    def test_callable(self):
        self.assertEqual(False, callable(42))
        self.assertEqual(False, callable('abcdefg'))
        self.assertEqual(True, callable(callable))


class MiscFunctionTestCase(unittest.TestCase):
    """
    Test debugger and misc. builtin function
    """
    def test_breakpoints(self):
        # call breakpoint() will bring you to pdb ...
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
