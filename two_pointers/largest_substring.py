from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return len('')
        largest_substring_indices = [0,0]
        substring_start_index = 0 
        characters_in_current_substring = dict()
        characters_in_current_substring[s[0]]=0
        for i in range(1,len(s)):
            if s[i] not in characters_in_current_substring.keys():
                #found a new substring from substring_start_index to i
                characters_in_current_substring[s[i]] = i 
                if i-substring_start_index > largest_substring_indices[1] - largest_substring_indices[0]:
                    largest_substring_indices = [substring_start_index,i]
            else:
                new_substring_start_index = characters_in_current_substring[s[i]] + 1
                #remove all of the characters that are in substring_start_index...new_substring_start_index
                for j in range(substring_start_index,new_substring_start_index):
                    del characters_in_current_substring[s[j]]
                characters_in_current_substring[s[i]] = i
                substring_start_index = new_substring_start_index 
        return len(s[largest_substring_indices[0]:largest_substring_indices[1]+1])




                



        