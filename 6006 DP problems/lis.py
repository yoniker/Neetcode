#LIS - top down

# Given one sequence:

# CARBOHYDRATE

# find the longest subsequence in this sequence which is increasing
# (in this case ABORT).






# Subproblem definition:

# LIS(i,last_value): given the sequence s[i:], and last_value_used which is the value of the last character that I've used when producing the current subsequence, produce the largest LIS such that every value that greater than last_value

# Original problem: LIS(0, None)


# Basecase: LIS(n,x)=''
# LIS(n-1,None) = s[n-1]

# Recursive relation:
# LIS(i,last_value)=
# if s[i]<last_value -return  LIS(i+1,last_value)

# if s[i]>last_value - return  max {
# LIS(i+1,last_value),
# s[i]+LIS(i+1),s[i])
# }

# Topology (index,last_value) where index is decreasing, and last_value is also decreasing

# Time:
# Number of subproblems:
# |S|*|alphabet| so if our alphabet is a constant, then time complexity is O(|S|), but what if in reality it's a huge number?

# But that last_value is taken from s, and therefore it's actually O(n^2) different subproblems.

s='CARBOHYDRATE'


mem_pad = dict()

def lis(i,last_value=None):
    #Base
    if i>=len(s):
        mem_pad[(i,last_value)] = ''
        return mem_pad[(i,last_value)]
    if last_value and s[i]<last_value:
        mem_pad[(i,last_value)] = lis(i+1,last_value)
        return mem_pad[(i,last_value)]
    take_ith_character = s[i]+lis(i+1,s[i])
    dont_take_ith_character = lis(i+1,last_value)
    max_len = take_ith_character if len(take_ith_character)>len(dont_take_ith_character) else dont_take_ith_character
    mem_pad[(i,last_value)] = max_len
    return mem_pad[(i,last_value)]

print(lis(0,None))
