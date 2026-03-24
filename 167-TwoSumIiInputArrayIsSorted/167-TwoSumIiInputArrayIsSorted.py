# Last updated: 24/03/2026, 22:38:52
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, value in enumerate(numbers):
            find = target - value
            if find in d:
                return [d[find]+1, i+1]
            d[value] = i
        return []