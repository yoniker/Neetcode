from typing import List

class Solution:
        

    def sortColors(self, nums: List[int]) -> None:
        # invariants: 
        # 1. to the left of current pointer, there are only 1s and 0s. 
        # 2. to the right of next_location_of_2s there are only twos.
        # 3. To the left of next_location_of_0s there are only 0s
        next_location_of_0s = 0
        next_location_of_2s = len(nums)-1
        current_index=0 #TODO see what happens for different starting values at location 0
        while current_index<=len(nums)-1:
            if nums[current_index] == 2:
                if current_index >= next_location_of_2s:
                    break
                nums[current_index],nums[next_location_of_2s] = nums[next_location_of_2s],nums[current_index]
                next_location_of_2s -= 1
                continue
            if nums[current_index] == 0:
                nums[current_index],nums[next_location_of_0s] = nums[next_location_of_0s],nums[current_index]
                next_location_of_0s += 1
                current_index += 1
                continue
            current_index += 1 