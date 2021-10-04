#<------------------------ Lecture 11 ------------------------------>
#<------------------------------------------------------------------>

"""L contains 1...n, except for some k

Find k efficiently.

The sum of 1 -> n = n(n+1)/2

L[0] -> L[len(L) - 1] is n = n(n+1)//2 - k

k = n(n+1)//2 - (L[0] + ... L[len(L)-1])
"""

def missing_k(L):
    n = len(L) + 1
    cur_sum = 0
    for e in L:
        cur_sum += e
    return n*(n+1)//2 - cur_sum

