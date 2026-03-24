# Last updated: 24/03/2026, 22:38:49
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than the length of nums
        nums[:] = nums[-k:] + nums[:-k]

        