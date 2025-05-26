from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        #         if i am the minimum,I want to try to 'improve myself', and that can be done with a greater heighet.
        # a greater height after k steps will yield (w-k)*(previous minimum+difference in height) AT BEST,so the new height needs to be at least K bigger for me to even consider this as a candidate.
        #in other words, it cannot be that I change something from the other side, which doesn't limit this product, and improve my result
        #if they are both of the same size, it doesn't matter which I try to change first.
        left_index = 0
        right_index = len(height) - 1
        current_max_container = 0
        while left_index < right_index:
            current_max_container = max(current_max_container,(right_index - left_index) * min (height[left_index],height[right_index]) )
            if min(height[left_index],height[right_index]) == height[left_index]: #Need to change the right index
                height_to_surpass = height[left_index]
                while left_index<right_index and height[left_index]<=height_to_surpass:
                    left_index+=1
            else:
                height_to_surpass=height[right_index]
                while left_index<right_index and height[right_index]<=height_to_surpass:
                    right_index-=1
        return current_max_container

        