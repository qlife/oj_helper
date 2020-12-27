import bisect
import collections


class Solution():
    @staticmethod
    def sol(A):
        s = frozenset([a for a in A if a > 0])

        if len(s) == 0:
            return 1
        else:
            m = max(s)

        # t = SET({ 1, .. , M, (M+1) })
        t = frozenset(range(1, m+2))
        d = t - s
        return min(d)


def main():
    s = Solution()
    print(s.sol([-1000, -3, -2, -1, 0, 1, 2, 5, 9]))
    print(s.sol([-1000, 1000]))
    print(s.sol([-1000]))
    print(s.sol([-1000, 0]))
    print(s.sol([0, 0, 0]))
    print(s.sol([-1000, -999, 0]))
    print(s.sol([1, 2, 3]))
    print(s.sol([2, 5, 8]))
    print(s.sol(list(range(2, 10001))))
    print(s.sol(list(range(1, 10000))))


if __name__ == '__main__':
    main()
