#<----------------------------------- Lecture 6 ----------------------------------->
#<------------- For Loops -------------->

"Used to repeat a block a number of times, and do something each time it repeats"

for i in range(5):
    print("I <3 EngSci")

for i in range(5):
    print( 2 * i )
    print(i)
    print("==========")

#a^n : a^a * ....... * a (n times)

def my_pow(a, n):
    '''Return a^n, where n is a non-negative integer'''
    prod = 1
    for i in range(n):
        prod = prod * a

    return prod


#<------------------- While Loops ------------------->

"""Repeat block while the condition is True

While condition:
    some code
    
"""

i = 0
while i < 5:
    print("hi", i)
    i = i + 1

#<------ Same thing as a for loop ------->
for i in range(5):
    print("hi", i)

#<------------ Compute log10(n) ----------->
# 10 ^ a = n, solve for a
# try 10^0, 10^1, 10^2, until you encounter 10 ^ a = n

def my_log(n):
    res = 1
    i = 0

    # When we're entering the loop, res = 10 ^ i
    while res < n:
        res = res * 10
        i += 1
    return i


for j in range(10):
    print(j)

#for i in range(start, stop, step)

for i in range(5, 14, 2):
    print(i)


#<---------- Problem Solving with Modulus ------------->
"""Write a function that returns True if the input n is prime, false otherwise"""

# 7 % 2 = 1
# 7/2, remainder 1

"""The first thing we could try is to divide by every number... not efficient at all. Instead...
"""

def is_prime(n):
    '''Return True iff n is prime, n is an integer'''
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, n):
        if n % 1 == 0:
            return False

    return True # This will only be reached if the other return statement is never passed

# A different way of doing it
def is_prime3(n):
    '''Return True iff n is prime, n is an int'''
    if n <= 1:
        return False
    if n ==2:
        return True

    for i in range(n-2):
        if n % (2+i) == 0:  #n=121, i = 9: n % (9+2) == 0
            return False
    
    #If we are here, that means that we never returned False, so we tried
    #all the possible factors and it turned out that 
    return True