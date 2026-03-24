# Last updated: 24/03/2026, 22:38:40
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for index, value in enumerate(nums):
          if (value in d) and (abs(index - d[value])) <= k:
            return True
          else:
            d[value] = index
        
        return False
        