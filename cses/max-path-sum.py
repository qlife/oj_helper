def main():
    m = [
        [3, 7, 9, 2, 7],
        [9, 8, 3, 5, 5],
        [1, 7, 9, 8, 5],
        [3, 8, 6, 4, 10],
        [6, 3, 9, 7, 8]
    ]

    n = len(m)

    # Important pattern!
    s = [[0 for _ in range(n)] for _ in range(n)]

    s[0][0] = m[0][0]
    for x in range(1, n):
        s[0][x] = s[0][x-1] + m[0][x]

    for y in range(1, n):
        s[y][0] = s[y-1][0] + m[y][0]

    for y in range(1, n):
        for x in range(1, n):
            print(y, x)
            s[y][x] = max(s[y-1][x], s[y][x-1]) + m[y][x]
            #
            # could skip these cases here, we've done previously.
            # elif y == 0:
            #     pass
            #
            # elif x == 0:
            #     pass

    print(s)
    print(s[n-1][n-1])


if __name__ == '__main__':
    main()
