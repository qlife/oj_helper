from io import StringIO


def solution(n):
    cout = StringIO()
    cout.write(str(n))
    while n != 1:
        if 0 == (n%2):
            n = n // 2
        else:
            n = 3 * n + 1
        cout.write(" ")
        cout.write(str(n))

    print(cout.getvalue())


if __name__ == '__main__':
    n = int(input())
    solution(n)