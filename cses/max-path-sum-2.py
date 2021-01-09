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

    # Important pattern!
    s = [[0 for _ in range(1+n)] for _ in range(1+n)]

    for y in range(1, n+1):
        for x in range(1, n+1):
            print(y, x)
            s[y][x] = max(s[y-1][x], s[y][x-1]) + m[y][x]

    print(s)
    print(s[n][n])


if __name__ == '__main__':
    main()
