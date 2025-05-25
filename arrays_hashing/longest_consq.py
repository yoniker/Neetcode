from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashed = {} # Save all of the numbers at a hashset, and then iterate over hashset,connecting all the connected parts. Since d(v)<=2 for all v, sum over that is 2*v at most, or 2*n
        for num in nums: #let's save [a] for an unconnected number a and [min,max] for a connected vertex which is connected to a segment between numbers min and max
            nums_hashed[num] = [num]
        max_segment_length = 0
        for num in nums:
            if len(nums_hashed[num])>1 : continue #we have seen this before - this is an unnessesary optimizing from computational time theory point of view
            a = b = num #[a,b] will be the biggest segment to which num belongs
            while len(nums_hashed.get(b+1,[])) >0:
                b = b+1
            while len(nums_hashed.get(a-1,[])) > 0 :
                a=a-1
            if a!=b: #it's a connected segment of size greater than one

                #update all vertices: also unnecessary from a computational time complexity point of view
                for i in range(a,b+1):
                    nums_hashed[i] = [a,b]
            if b-a+1>max_segment_length:
                max_segment_length = b-a+1
        return max_segment_length

                
            


        
        