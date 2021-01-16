"""
Combined knowledge

Max path sum
Reconstruction the solution path
Creation of Python 2D list
"""


def main():
    m = [
        [0, 0, 0, 0, 0, 0],
        [0, 3, 7, 9, 2, 7],
        [0, 9, 8, 3, 5, 5],
        [0, 1, 7, 9, 8, 5],
        [0, 3, 8, 6, 4, 10],
        [0, 6, 3, 9, 7, 8]
    ]

    n = 5
    N = 1 + n
    s = [[0 for _ in range(N)] for _ in range(N)]
    d = [['X' for _ in range(N)] for _ in range(N)]

    for j in range(1, N):
        for i in range(1, N):
            s[j][i] = max(s[j-1][i], s[j][i-1]) + m[j][i]
            d[j][i] = 'U' if s[j-1][i] > s[j][i-1] else 'L'

    print(s)
    print(s[n][n])  # not m[N][N] ! It is m[1+n][1+n]

    # rebuild the path
    res = []
    x, y = n, n
    # Why not choose x == 1 and y == 1 ?
    # Yes, in that case we lost the original point d[1][1]
    while not (x == 1 and y == 1):
        # for debug purpose
        # print((y, x))
        res.append((y, x))
        direction = d[y][x]
        if direction == 'U':
            y -= 1
        elif direction == 'L':
            x -= 1
        else:
            print(res)
            assert False
    else:
        # Loop ends when x == 1 and y == 1,
        # so we add the start of path in this moment.
        res.append((1, 1))

    # We reconstruct the path from the end of the path,
    # so we print it from the end of list `res[]`
    for j in range(len(res)-1, 0-1, -1):
        print(res[j], m[res[j][0]][res[j][1]])


if __name__ == '__main__':
    main()
