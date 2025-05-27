class Solution:


    def minWindow(self, s: str, t: str) -> str:
        negative_differences = dict()
        characters_count_t = dict()
        for c in t:
            characters_count_t[c] = characters_count_t.get(c,0) + 1
            negative_differences[c] = negative_differences.get(c,0) -1
        positive_differences = dict()
        l,r = 0,-1
        current_min_window = None

        while l<len(s) and r<len(s):
            #Either the current window s[l:r+1] containts t or not
            if len(negative_differences) != 0: #Current window doesn't contain t
                r+=1
                if(r>=len(s)):
                    continue
                #update the differences dictionations if the character is in t
                if characters_count_t.get(s[r],0) !=0: #if the character does not appear in t, i don't need to update the differences datastructures
                    if negative_differences.get(s[r],0)!=0:
                        if negative_differences[s[r]]==-1:
                            del negative_differences[s[r]]
                        else:
                            negative_differences[s[r]] += 1
                    else:
                        positive_differences[s[r]] = positive_differences.get(s[r],0) + 1
            else: #Current window contains t
                
                if characters_count_t.get(s[l],0)!= 0 : #I want 'delete' the character from the table only if it is in t
                    if positive_differences.get(s[l],0)>0:
                        if positive_differences[s[l]] == 1:
                            del positive_differences[s[l]]
                        else:
                            positive_differences[s[l]] -=1
                    else:
                        negative_differences[s[l]] = -1
                l+=1

            

            if len(negative_differences) == 0:
                if current_min_window is None:
                    current_min_window = (l,r)
                else:
                    if current_min_window[1]-current_min_window[0]+1>r-l+1:
                        current_min_window = (l,r)

        if current_min_window is None:
            return ''
        return s[current_min_window[0]:current_min_window[1]+1]






