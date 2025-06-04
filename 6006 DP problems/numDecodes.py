#a DP Solution for this question: https://leetcode.com/problems/decode-ways/
#Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0
#decoding are just from 1...26 to A...Z but 112 can be [1,1,2] [11,2] or [1,12]
#in the end, this is nothing but a fancy extension to Fibonnaci numbers
# Time: number of subproblems is O(len(s)) and each subproblem takes (without recursive calls) O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        memPad = dict()
        def numDecodes(i): #How many ways to decode the string starting at index i do i have
            if i>=len(s):
                return 1
            if i in memPad:
                return memPad[i]

            if s[i]=='0':
                memPad[i] = 0 #if it starts with 0, cannot interpret it in a legal way
                return memPad[i]
            if i==len(s)-1:
                memPad[i] = 1
                return memPad[i]
            if ord(s[i])>ord('2'): #If first character is greater than 2, i have only one way to decode it
                memPad[i] = numDecodes(i+1)
                return memPad[i]
            if s[i] == '1': #If it is 1, then no matter what the next character is, I can interpret them together, and I can (try to) interpret s[i] by itself.
                memPad[i] = numDecodes(i+1)+numDecodes(i+2)
                return memPad[i]
            if s[i]=='2':
                if ord(s[i+1])<=ord('6'):#20...26 i can decode it in two way
                    memPad[i] = numDecodes(i+1) + numDecodes(i+2)
                    return memPad[i]
                memPad[i] = numDecodes(i+1)
                return memPad[i]
        return numDecodes(0)
