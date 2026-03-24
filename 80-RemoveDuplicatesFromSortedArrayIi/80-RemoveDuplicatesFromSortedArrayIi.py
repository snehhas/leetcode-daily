# Last updated: 24/03/2026, 22:39:21
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        count=1
        while i<len(nums):
            if nums[i-1]==nums[i]:
                count+=1
                if count>2:
                    nums.pop(i)
                    i-=1
            else:
                count=1
            i+=1
        return len(nums)