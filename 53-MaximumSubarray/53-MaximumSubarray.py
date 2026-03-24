# Last updated: 24/03/2026, 22:39:32
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pf=float('-inf')
        sum_=0
        for i in nums:
            sum_+=i
            pf=max(pf,sum_)
            if sum_<0:
                sum_=0
        return pf