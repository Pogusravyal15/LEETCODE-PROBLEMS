class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            n = n * 10 + digit
            temp //= 10
        return n == x