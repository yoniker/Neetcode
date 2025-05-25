from typing import List

class Solution:

    #In Leetcode it wants me to use the least amount of space, but i will use mergesort which is O(n) in space anyways, because Heapsort I'll implement later (seems like an overkill for now)

    def _mergeSortedArrays(self,array1:List[int],array2:List[int]):
        index1 = 0
        index2 = 0
        newMergedArray = []
        while index1<=len(array1)-1 and index2<=len(array2)-1:
            if array1[index1] < array2[index2]:
                newMergedArray.append(array1[index1])
                index1+=1
            else:
                newMergedArray.append(array2[index2])
                index2+=1
        while index1<=len(array1)-1:
            newMergedArray.append(array1[index1])
            index1+=1
        while index2<=len(array2)-1:
            newMergedArray.append(array2[index2])
            index2+=1
        return newMergedArray
    



    def sortArray(self, nums: List[int]):
        if len(nums) <=1:
            return nums
        middleIndex = len(nums) // 2
        array_left = self.sortArray(nums[0:middleIndex])
        array_right = self.sortArray(nums[middleIndex:])
        newSortedArray = self._mergeSortedArrays(array_left,array_right)
        return newSortedArray
    
