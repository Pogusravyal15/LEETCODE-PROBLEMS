from typing import List
class Solution:
    def countStudents(self, student: List[int], sandwitch: List[int]) -> int:
        count = Counter(student)
        for s in sandwitch:
            if count[s] > 0:
                count[s] -= 1
            else:
                return count.total()
        return 0  