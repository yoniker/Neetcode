#This code is faster than 97% of leetcode
#That being said, I don't like it as it's awkward and not elegant

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def maxProductNoZero(indexFrom,indexTo):
            #This will calculate the max product of the sub array 
            #num[i:j+1] assuming that  all integers in array are not 0
            if indexFrom == indexTo:
                return nums[indexFrom]
            indexOfFirstNegative = -1
            indexOfLastNegative = -1
            numberOfNegativeNumbers = 0
            for index in range(indexFrom,indexTo+1):
                if nums[index]<0:
                    numberOfNegativeNumbers+=1
                    if indexOfFirstNegative == -1:
                        indexOfFirstNegative = index
                    else: #I saw a negative number before
                        indexOfLastNegative = index
            if numberOfNegativeNumbers % 2 == 0:
                #Return the product of the entire subarray
                ans=1
                for index in range(indexFrom,indexTo+1):
                    ans*=nums[index]
                return ans
            ansBefore = 1
            ansAfter = 1
            range_before,range_after = None,None
            if numberOfNegativeNumbers == 1:
                range_before=range(indexFrom,indexOfFirstNegative)
                range_after= range(indexOfFirstNegative+1,indexTo+1)
            else:
                range_before=range(indexFrom,indexOfLastNegative)
                range_after=range(indexOfFirstNegative+1,indexTo+1)
                
            for i in range_before:
                ansBefore*=nums[i]
            for i in range_after:
                ansAfter*=nums[i]
            return max(ansBefore,ansAfter)
            


        
        if len(nums)==0:
            return 1
        maxSoFar = nums[0]
        currentNonZeroRange = 0
        current_index = 0
        while current_index<len(nums):
            if nums[current_index]==0:
                if current_index !=currentNonZeroRange:
                    maxSoFar=max(0,maxSoFar,maxProductNoZero(currentNonZeroRange,current_index-1))
                currentNonZeroRange = current_index+1
            current_index+=1
        print(f'{current_index} {currentNonZeroRange}')
        if current_index>currentNonZeroRange:
            maxSoFar=max(maxSoFar,maxProductNoZero(currentNonZeroRange,current_index-1))
        return maxSoFar
        