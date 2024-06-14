from typing import List
class Solution:
    def decode(self, A: List[int], first: int) -> List[int]:
        ans = [first]
        n = len(A)
        for i in range(n):
            a = ans[-1] ^ A[i]
            ans.append(a)
        return ans