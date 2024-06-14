from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        C=""
        indices=list(indices)
        for i in range(len(s)):
            b=indices.index(i)
            C+=s[b]
        return C