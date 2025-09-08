class Solution:
    def sumOfUnique(self, nums):
        d = {}
        ans = 0

        # Count frequency of each number
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # Add only numbers that appear once
        for k, v in d.items():
            if v == 1:
                ans += k

        return ans

