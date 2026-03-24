# Last updated: 24/03/2026, 22:38:50
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        c=Counter(nums)

        for key,value in c.items():
            if value>n:
                return key
