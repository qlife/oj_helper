class Solution:
    """
Testcases
123
-123
120
0
2147483647
-2147483647

Expected:
321
-321
21
0
0
0
    """
    def reverse(self, x: int) -> int:
        # Case #1 0
        # Case #2 -2**31 - surely 0
        if x == 0 or x == (-2 ** 31):
            return 0
        elif x < 0:
            # Case #3 recursively call to handle negative input
            return 0 - self.reverse(-x)

        digit, rev = 0, 0
        overflow_limit = ((2 ** 31) - 1) // 10

        while x > 0:
            digit = x % 10
            # Overflow checks:
            # rev * 10 > MAX_INT <=> rev > (MAX_INT/10)
            if rev > overflow_limit:
                return 0
            rev = rev * 10 + digit
            # Python has operator (//=) !
            # x //= y equals to x = x // y
            x //= 10

        return rev
