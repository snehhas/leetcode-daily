# Last updated: 24/03/2026, 22:38:33
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_of_0, prod, prod_arr=0, 1, []
        for i in nums:
            if i==0:
                count_of_0+=1
        if count_of_0>1:
            return [0]*len(nums)

        for i in range(len(nums)):
            if count_of_0==1:
                if nums[i]==0:
                    index=i
                    continue
                prod*=nums[i]
            else:
                prod*=nums[i]
        if count_of_0==1:
            arr=[0]*len(nums)
            arr[index]=prod
            return arr
        else:
            prod_arr=[prod]*len(nums)
            return [prod_arr[i]//nums[val] for val in range(len(nums))]


        
        