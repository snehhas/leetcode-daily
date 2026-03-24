# Last updated: 24/03/2026, 22:38:42
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,curr, best = -1,0,float('inf')
        val=False
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>=target:
                l+=1
                curr-=nums[l]
                best=min(best,r-l+1)
                val=True
        if val:
            return best
        else:
            return 0