# Last updated: 24/03/2026, 22:39:07
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(set(nums))
        lastNum = nums[0]
        curLength = 1
        res = 1
        
        for i in range(1, len(nums)):
            if nums[i] == lastNum + 1:
                curLength += 1
            else:
                curLength = 1
            res = max(res, curLength)
            lastNum = nums[i]
            
        return res