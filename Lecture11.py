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

"""Return first even element in L"""

def first_even(L):
    '''Return the first even element of L'''
    for e in L:
        if e % 2 == 0:
            return e

def first_two_evens(L):
    '''Return the first two even elements of L'''
    res = []
    for e in L:
        if e % 2 == 0:
            res.append(e)
    
    return res[:2]

def first_two_evens_better(L):
    '''Return the first two even elements of L'''
    res = []
    for e in L:
        if e % 2 == 0:
            res.append(e)
            if len(L) == 2:
                return res


#<------------ Unrolling loops ---------->
counter = 0
for i in range(3):
    for j in range(2):
        counter += 1
        print("i =", 1, ". j=", j, ". counter =", counter)

# This is unrolling the loop, it explains how the loop works, generally only used in closer component languages and on logic boards.
i = 0
for j in range(2):
    counter += 1
    print("i =", 1, ". j=", j, ". counter =", counter)

i = 1
for j in range(2):
    counter += 1
    print("i =", 1, ". j=", j, ". counter =", counter)

i = 2
for j in range(2):
    counter += 1
    print("i =", 1, ". j=", j, ". counter =", counter)


def iter_j(i):
    global counter
    for j in range(2):
        counter += 1
        print("i =", 1, ". j=", j, ". counter =", counter)

def iter_j_counter(i, counter):
    for j in range(2):
        counter += 1
        print("i =", 1, ". j=", j, ". counter =", counter)
    
    return counter
    

if __name__ == '__main__':
    counter = 0
    for i in range(3):
        iter_j(i)


#<-------------------------------------------------------------------------------------------------------------------------------->
def login(username, password):
    if username == "guerzhoy" and password == "adbc":
        return True
    else:
        return False

"""Try every possible password, and print the correct password for guerzhoy, assuming the length of the password is 4"""
def password():
    for letter1 in ["a", "b", "c", "d", "e", "f"]:
        for letter2 in ["a", "b", "c", "d", "e", "f"]:
            for letter3 in ["a", "b", "c", "d", "e", "f"]:
                for letter4 in ["a", "b", "c", "d", "e", "f"]:
                    password = letter1 + letter2 + letter3 + letter4
                    print("Trying password", password)
                    if login("guerzhoy", password):
                        print("The password is", password)
                        return password


"""Here is a fun, stupid way of breaking that guerzhoy insisted on using."""
breaknow = False
def password2():
    for letter1 in ["a", "b", "c", "d", "e", "f"]:
        if breaknow:
            break
        for letter2 in ["a", "b", "c", "d", "e", "f"]:
            if breaknow:
                break
            for letter3 in ["a", "b", "c", "d", "e", "f"]:
                if breaknow:
                    break
                for letter4 in ["a", "b", "c", "d", "e", "f"]:
                    if breaknow:
                        break
                    password = letter1 + letter2 + letter3 + letter4
                    print("Trying password", password)
                    if login("guerzhoy", password):
                        return password
                        breaknow = True
password()

"""Here's another way"""
alphabet = ["a", "b", "c", "d", "e", "f"]
breaknow = False
il = 0
while il < 6 and not breaknow:
    letter1 = alphabet[il]
    i2 = 0
    while il < 6 and not breaknow:
        None #"""Add the code here for the rest of it"""


# L = [1, 5, 6, 1, 7, 9]
def has_duplicates(L):
    '''Return True if L has duplicate elements
    [1, 5, 6, 1, 7, 9]  ---> True
    [5, 6, 1, 7, 9] ---> False'''

    for i in range(len(L)):
        if L[i] in L[i+1:]:
            return True

def has_duplicates_fast(L):
    '''Return True if L has duplicate elements
    [1, 5, 6, 1, 7, 9]  ---> True
    [5, 6, 1, 7, 9] ---> False'''
    L2 = sorted(L)
    for i in range(len(L)):
        if L2[i] == L2[i+1]:
            return True

sq = [[2, 9, 4],
        [1, 5, 6],
        [7, 8, 7]]

def has_duplicates_sq(sq):
    sq_flat= []
    for line in sq:
        sq_flat.extend(line)
        return has_duplicates_fast(sq_flat)