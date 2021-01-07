import unittest


class SyntaxTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.context = dict(x=1)

    def test_unary_inc_op(self):
        # Use the context manager return by assertRaises
        with self.assertRaises(SyntaxError) as cm:
            print(cm)
            eval('x++', self.context)

    def test_unary_dec_op(self):
        """
        Explain the parameters:

        self.assertRaises(exception: tuple or one exception,
                            callable,
                            *arg,
                            **kwds)
        """
        # Deliberately using list expansion
        self.assertRaises((SyntaxError, ), eval, *('x--', self.context))

    def test_question_mark_op(self):
        self.assertRaises(SyntaxError, eval, 'x > 0 ? 1 : 2', self.context)


if __name__ == '__main__':
    unittest.main()
