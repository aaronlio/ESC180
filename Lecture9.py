import random

# You can use random.random() to get random numbers

x1 = random.random()
x2 = random.random()

x1, x2 = random.random(), random.random()

"""We can use the Monte Carlo method to develop an approximation of pi.
"""

def approx_pi(n_points):
    '''Use n_points random points to approximate pi using a Monte Carlo method'''
    count = 0
    for i in range(n_points):
        x1, x2 = random.random(), random.random()

        if x1**2 + x2**2 < 1:
            count += 1
        
    return 4 * count / n_points

if __name__ == '__main__':
    print(approx_pi(400000))


# <------ Random Number Generator, partially missed this, check lecture notes --------->

def f(x):
    global x
    return (345345345435*x) % 59

def my_random():
    global x
    x = f(x)
    return x/59

def initialize():
    global x1
    x = 3

if __name__ == '__main__':
    initialize()
    print(my_random())

# <---------- List Slicing ----------->
L = [5, 10, 12, 59, 12,23]
#L[start:end:step]
L[1: 4: 2]  # [10, 59]


"""This function uses the start value, checks if i is less than the end value, we take the value at index i and 
increment by step
"""
def slice_manual_while(L, start, end, step):
    '''Return L[start:end:step]'''

    res = []
    i = start
    if step > 0:
        while i < end:
            res.append(L[i])
            i += step
    else:
        # this is used in case where 
        while i > end:
            res.append(L[i])
            i += step
    
    return res

    # (step > 0 and i < end) or (step < 0 and i > end) is the condition you're checking for


#<-------------------- Extend Vs Append -------------------->
L.extend(L1) # appends every element of L1 to L
L = [1,2,3]
L1 = [6,7]
"""Append would create a nested list, which is not what we want"""

# Extending in the middle...these 3 lines will insert L1 into L
L = [1,2,3]
L1 = [6,7]
L[1:1] = L1

# if it happend to say L[1:2], the second value of L would've been replaced *think about indexing*

#<------------------ .sort() and sorted() ------------------->
"""Sorts numerically or alphabetically. 
.sort() changes the values of the list, sorted does not"""

#<----------------- Other list details --------------->
[4, 5, 6] + [2, 3] #[4, 5, 6, 2, 3]

L = [7, 8, 9]
L += [7, 8, 9] # same as extend, changes the value of L