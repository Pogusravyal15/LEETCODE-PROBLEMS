from typing import List
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        total = 0
        for i in range(len(words)):
            if words[i][::-1] in (words[i+1:]):
                total+=1
        return total