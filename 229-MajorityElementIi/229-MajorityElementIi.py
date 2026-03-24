# Last updated: 24/03/2026, 22:38:37
from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums) // 3
        d = defaultdict(int)  # Initialize defaultdict with default type of int
        
        # Count occurrences of each number in nums
        for num in nums:
            d[num] += 1
        
        # Find numbers with counts greater than length
        result = [num for num, count in d.items() if count > length]
        return result
