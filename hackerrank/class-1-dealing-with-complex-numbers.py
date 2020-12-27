import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        self.real += no.real
        self.imaginary += no.imaginary

    def __sub__(self, no):
        self.real -= no.real
        self.imaginary -= no.imaginary

    def __mul__(self, no):
        self.real = self.real * no.real - self.imaginary * no.imaginary
        self.imaginary = self.real * no.imaginary + self.imaginary * no.real

    def __truediv__(self, no):
        rhs_re = no.real
        rhs_im = no.imaginary

        conjugate_re = rhs_re
        conjugate_im = -rhs_im

        denominator = rhs_re * conjugate_re - rhs_im * conjugate_im

        self.real = (self.real * rhs_re - self.imaginary * rhs_im) / denominator
        self.imaginary = (self.real * conjugate_im + self.imaginary * conjugate_re) / denominator

    def mod(self):
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    # c = map(float, input().split())
    # d = map(float, input().split())
    # x = Complex(*c)
    # y = Complex(*d)
    x = Complex(2, 1)
    y = Complex(5, 6)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
    # TODO