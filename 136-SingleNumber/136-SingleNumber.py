# Last updated: 24/03/2026, 22:39:03
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_arr = 0
        for i in range(0,len(nums)):
            xor_arr = xor_arr ^ nums[i]
        return xor_arr