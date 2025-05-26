class Solution:
    def isReplaceableWindow(self,current_window,k,max_character_count):
        current_window_size = current_window[1]-current_window[0]+1
        number_of_characters_different_than_max = current_window_size - max_character_count
        return number_of_characters_different_than_max <= k
    def findMaxCharacter(self,characters_count):
        max_character = ''
        for key,value in characters_count.items():
            if value > characters_count.get(max_character,0):
                max_character=key
        return max_character
    
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) ==0 : return 0
        current_window_characters_count = {s[0]:1}
        current_max_replaceable_window = (0,0)
        current_window_max_character = s[0]
        start_index_current_window = 0
        for i in range(1,len(s)):
            if s[i]==current_window_max_character:
                current_window_characters_count[s[i]] +=1
                if i-start_index_current_window+1 > current_max_replaceable_window[1] - current_max_replaceable_window[0] + 1:
                    current_max_replaceable_window = (start_index_current_window,i)
            else:
                current_window_characters_count[s[i]] = current_window_characters_count.get(s[i],0)+ 1
                if current_window_characters_count[s[i]] > current_window_characters_count[current_window_max_character]:
                    current_window_max_character = s[i]
                #Let's check if current window is legit in the sense of replacing k characters will yield a repeated character string
                
                while not self.isReplaceableWindow(current_window = (start_index_current_window,i),k=k,max_character_count=current_window_characters_count[current_window_max_character]):
                    current_window_characters_count[s[start_index_current_window]] -=1 
                    start_index_current_window+=1
                    current_window_max_character = self.findMaxCharacter(current_window_characters_count)

                if i-start_index_current_window+1 > current_max_replaceable_window[1] - current_max_replaceable_window[0] + 1:
                        current_max_replaceable_window = (start_index_current_window,i)
        return current_max_replaceable_window[1]-current_max_replaceable_window[0]+1