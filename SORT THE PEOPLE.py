from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans=zip(heights,names)
        l=[]
        for i, j in sorted(ans):
            l.append(j)
        return l[::-1]
