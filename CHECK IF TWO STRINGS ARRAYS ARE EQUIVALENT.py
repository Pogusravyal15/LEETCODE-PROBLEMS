from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        joined_word1 = "".join(word1)
        joined_word2 = "".join(word2)
        if (joined_word1==joined_word2):
            return True
        else:
            return False    