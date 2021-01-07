class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        # 2147483647 - 10 digits!
        modulo = [10 ** i for i in range(11)]
        for j in range(11):
            if modulo[j] > x:
                break
        digits = [(x % modulo[k + 1]) // modulo[k] for k in range(0, j)]
        print(j, digits)
        n = len(digits)
        for l in range(n // 2):
            if digits[l] != digits[n - l - 1]:
                return False
        else:
            return True
