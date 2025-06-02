#LCS- TOP DOWN
#Given two strings, find the largest common subsequence of both strings
#a subsequence can be created from any monotone increaing sequence of indices
#so HELLO is a subsequence of SDFHSDFELLO


mem_note = dict() #dictionary with all previous results



# I will define LCS as LCS(s1[:i],s2[:j])

s1 = "HIEROGLYPHOLOGY"
s2 = "MICHAELANGELO"
def lcs(i,j):
    if j<=0 or i<=0:
        return ''
    if (i,j) in mem_note:
        return mem_note[(i,j)]
    if s1[i-1]==s2[j-1]:
        mem_note[(i,j)] = lcs(i-1,j-1) + s1[i-1]
        return mem_note[(i,j)]
    left = lcs(i-1,j)
    right = lcs(i,j-1)
    if len(left)>len(right):
        mem_note[(i,j)] = left
        return mem_note[(i,j)]
    mem_note[(i,j)] = right
    return mem_note[(i,j)]

print(lcs(len(s1),len(s2)))
    