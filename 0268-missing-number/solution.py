class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        S=sum(nums)
        missing_num=n*(n+1)//2-S
        return missing_num
        
