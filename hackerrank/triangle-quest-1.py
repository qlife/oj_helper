# More than 2 lines will result in 0 score. Do not leave a blank line also

def sol1():
    for i in range(1, int(input())):
        print(i *
            ((10**8 * int(i >= 9)) + (10**7 * int(i >= 8)) +
             (10**6 * int(i >= 7)) + (10**5 * int(i >= 6)) +
             (10**4 * int(i >= 5)) + (10**3 * int(i >= 4)) +
             (10**2 * int(i >= 3)) + (10**1 * int(i >= 2)) +
             (10 ** 0 * int(i >= 1))))


def sol_pure_math():
    for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print((10 ** (i) // 9) * i)


def sol_random_access():
    for i in range(1, int(input())):
        print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])

sol1()