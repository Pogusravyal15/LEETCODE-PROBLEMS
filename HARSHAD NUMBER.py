class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        result = 0
        temp = x
        while temp != 0:
            result += temp % 10
            temp=temp // 10
        if x % result == 0:
            return result
        else:
            return -1
