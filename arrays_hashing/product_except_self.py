from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]):
        #I will calculate three different arrays in two passes:
        #1. Product of all elements before Xi and xi
        #2. Product of all elements after Xi and xi
        #3. the location of element 0 (if more than 1 then return array of 0s)
        location_of_0 = -1
        for i in range(len(nums)):
            if nums[i] ==0:
                if location_of_0!=-1:
                    return [0 for _ in range(len(nums))]
                location_of_0 = i
        product_to_left = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
        
            if i-1>=0:
                product_to_left[i] = product_to_left[i-1] * nums[i]
            else:
                product_to_left[i] = nums[i]
        product_to_right = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            if i+1<=len(nums)-1:
                product_to_right[i] = product_to_right[i+1] * nums[i]
            else:
                product_to_right[i] = nums[i]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if location_of_0!=-1 and location_of_0!=i:
                continue
            xi = 1
            if i+1<=len(nums)-1:
                xi*=product_to_right[i+1]
            if i-1>=0:
                xi*=product_to_left[i-1]
            ans[i] = xi
        return ans
            
        

        