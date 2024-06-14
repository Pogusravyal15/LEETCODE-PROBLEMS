class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew_list=list(jewels)
        answer=0
        for j in jew_list:
            answer+=stones.count(j)
        return answer