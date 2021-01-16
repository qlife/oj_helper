def solution():
    s = input().strip()
    ns, max_len, curr = len(s), 1, 1
    # curr == 1 means len of s[0]
    # Take max_len as minimum possible value 1

    if ns < 2:
        print(ns)
        return

    for i in range(1, ns):
        if s[i-1] == s[i]:
            curr += 1
            if max_len < curr:
                max_len = curr
        else:
            curr = 1
    else:
        print(max_len)


if __name__ == '__main__':
    solution()
