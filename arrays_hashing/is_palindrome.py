class Solution:
    def isPalindrome(self, s: str) -> bool:
        checked_str = []
        for c in s:
            c=c.lower()
            if (ord(c)>=ord('a') and ord(c) <=ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9')):
                checked_str.append(c)
        index_left,index_right = 0,len(checked_str)-1
        while index_left<index_right:
            if checked_str[index_left]!=checked_str[index_right]:
                return False
            index_left +=1
            index_right -=1
        return True

        