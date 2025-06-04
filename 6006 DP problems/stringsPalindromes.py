class Solution:
    def longestPalindrome(self, s: str) -> str:
        mempad= dict()
        def largestPalindrome(li,ri): #largest palindrome of s[li:ri+1]
            if li>ri:
                return ''
            if li==ri:
                return (li,ri)
            if (li,ri) in mempad:
                return mempad[(li,ri)]
            index_left = li 
            index_right = ri
            while (index_left<index_right and s[index_left]==s[index_right]):
                index_left += 1
                index_right -= 1
            if index_left>=index_right:
                mempad[(li,ri)] = (li,ri) #The entire substring is a palindrome
                return mempad[(li,ri)]
            #By removing just the first character and then checking all substrings, and then removing the last character and checking all substrings, I ensure that i check all
            option1 = largestPalindrome(li+1,ri) #explore all options without the first character
            option2 = largestPalindrome(li,ri-1)  #explore all options without the last character
            option1Length = option1[1] - option1[0]
            option2Length = option2[1] - option2[0]
            mempad[(li,ri)] = option1 if option1Length>=option2Length else option2
            return mempad[(li,ri)]
        ansFrom,ansTo = largestPalindrome(0,len(s)-1)
        return s[ansFrom:ansTo+1]


        


print(Solution().longestPalindrome("forgeeksskeegfor"))