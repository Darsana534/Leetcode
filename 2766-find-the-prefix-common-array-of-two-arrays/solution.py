from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count = [0] * (n + 1)  # track how many times each number has been seen
        prefix_common = 0
        ans = []

        for a, b in zip(A, B):
            # process element from A
            count[a] += 1
            if count[a] == 2:
                prefix_common += 1

            # process element from B
            count[b] += 1
            if count[b] == 2:
                prefix_common += 1

            ans.append(prefix_common)

        return ans
