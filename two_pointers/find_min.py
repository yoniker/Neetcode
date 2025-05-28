#find min in a rotated array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        indexSection1,indexSection2 = 0,len(nums)-1
        while nums[indexSection1]>nums[indexSection2] and indexSection2>indexSection1+1:
            middle_index = (indexSection1+indexSection2)//2
            if nums[middle_index]<nums[indexSection1]:
                indexSection2 = middle_index
            else:
                indexSection1 = middle_index
        return min(nums[indexSection1],nums[indexSection2])
        