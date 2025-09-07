class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        duplicate = sum(nums) - sum(set(nums))
        missing = sum(range(1, n + 1)) - sum(set(nums))
        return [duplicate, missing]
