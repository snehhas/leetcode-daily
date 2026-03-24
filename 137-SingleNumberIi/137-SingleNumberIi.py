# Last updated: 24/03/2026, 22:39:01
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once=seen_twice=0
        for num in nums:
            seen_once=~seen_twice&(seen_once^num)
            seen_twice=~seen_once&(seen_twice^num)
        return seen_once