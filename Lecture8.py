#<----------------------------------------- Lecture 8 --------------------------------------------->
#--------------------------------------------------------------------------------------------------->

#<------------------------->>

#n! = 1*2*3*4....* n

"""Compute the number of trailing zeros in n!
problem: computing n! for large n is very slow

n! = 1*2*3....*5...*(2*5)....*(3*5) * (5*5).... """

def multiplicity(n, k):
    '''Return the multiplicity of k in n
    (n = .....k^m*..... return m
    '''
    count = 0
    while n % k == 0:
        n //= k
        count += 1

def trailing_zeros_fast(n):
    '''Return the number of trailing zeros in n!
    '''

    factors5 = 0
    for i in range(1, n+1):
        factors5 += multiplicity(i, 5)

    return factors5

# Figure this out ^


#<---------- A function that checks whether the items in a list are increasing, not strictly though ----------->
def is_non_decreasing(L):
    '''Return True if L is a non-decreasing list. False o/w
    >>> is_non_decreasing([1, 2, 3, 3, 5] -> True
    >>> is_non_decreasing([1, 2, 3, 2, 5]) -> False 
    '''
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return False

    return True

# This is the same, just using different/my preferred indexing patterns (see range()) and line 50)
def is_non_decreasing(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False

    return True


#<------------------------------ Objects and Lists ------------------------------>
def f(x):
    return x **2

"""Lists can be homogenous (all the same type, ie. strings), or heterogenous (ie. strings and floats)"""

L = [4, "hello", f, 2]

"""Lists can also be *nested* within other lists, which means a structure within another structure:
"""
L = [42, 43, [45, 46], 47]

"""To access 45, we can use L[2][0], which is called double indexing. It works the exact same as normal indexing. 
The following example is also a nested list, it's just reformatted in a nicer way.
"""

L = [[1,2,3,4],
     [1,0,1,0],
     [2,2,3,5]]

# L[2] --> [2,2,3,5]
# L[2][3] --> 5

L = [[[[]]]]
#L[0] = [[[]]]
# L[0][0] = [[]]
# L[0][0][0] = []

#<---------------- Append(), insert(), and index() -------------------->
"""Values can be inserted into a list using the insert() or append() built-in functions"""

L = [5, 6, 10, 2]

#L.insert(ind,elem) #insert element before index ind
L.insert(2, 42)

#L = [5, 6, 42, 10, 2]

L = [5, 6, 10, 2]

#L.append(elem) adds an element to the end of a list
L.append(150)

# L = [5, 6, 10, 2, 150]

"""There's also a function index(), that returns the index of a value in a list,
if there are two of the values, it returns the index of the first occurance of the value"""

L = [5, 6, 10, 2]
L.index(6) # --> 1

"""We can also get bools to see if a given element is in a list"""
6 in L # --> True
12 in L # --> False

6 not in L # False
12 not in L # True

#< ------------------------>
e = 6
if e in L:
    print("The index of e in L is", L.index(e))
else:
    print("e is not in L")

#<------------------------ Creating Lists with list() -------------------->
"""We can use the list() built-in to create a list. For example:
"""

list(range(2, 10, 2))

# A different way to do the same thing

L = []
for i in range(2, 10, 2):
    L.append(i)

#<---------------- List Slicing ---------------->
L = [5, 6, 10, 2, 12, 50, 12, 40, 50, 10]
L[1:8:2] #--> [6, 2, 50, 40]
L[9:3:-1] #--> [10, 50, 40, 12, 50, 12]

L[::2] # --> [5, 10, 12, 12, 50]

def slice_manual(L, start, end, step):
    res = []
    for i in range(start, end, step):
        res.append(L[i])
    return res