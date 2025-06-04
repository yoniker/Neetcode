#solve subset sum DP - Top down

subset = [2,5,7,8,9]
memo_pad = {}
def can_sum(i,v):

    if v<0: return False
    if v==0: return True
    if i>=len(subset): return False

    if (i,v) in memo_pad:
        return memo_pad[(i,v)]
    

    memo_pad[(i,v)] =   can_sum(i+1,v-subset[i]) or can_sum(i+1,v)
    return memo_pad[(i,v)]

print(can_sum(0,25))
print(can_sum(0,21))