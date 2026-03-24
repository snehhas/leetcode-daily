# Last updated: 24/03/2026, 22:38:41
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        arr={}
        for i in nums:
            try:
                if arr[i]:
                    return True
            except:
                pass
            arr[i]=1
        return False