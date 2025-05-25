from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index_left = 0
        index_right = len(s)-1
        while index_left < index_right:
            s[index_left],s[index_right] = s[index_right], s[index_left]
            index_left += 1
            index_right -=1
# arr = ["h","e","l","l","o"]
# Solution().reverseString(arr)
# print(arr)
        