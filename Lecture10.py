import math

#<-------------------------------------- Variable Names ------------------------------------------>
"""Legal variable names begin with letters
If your variable is multiple words, you can either use camelCase or underscore_casing

You generally want to be descriptive with your variable names
"""

#<---------------- Infinite Loops --------------------->
"""Loops that run forever:

while True:
    print("Praxis!")
    
"""


#<------------------ Interview Puzzle -------------->

"""Given a list L than contains the number 1 --> n in some order, but with k missing, determine k"""

missing_k = (1,2,4,5)
#print(math.sum(missing_k))
# can find n = len(L) + 1
# do that using just a single pass over the list L

def missing_k(L):
    for i in range(1, len(L) + 1):
        if i not in L:
            return i

def better_missing_k(L):
    return (len(L)+1**2/2) - sum(L)


#<--------------------- Nested Loops --------------------->
counter = 0
for i in range(3):
    for j in range(2):
        counter += 1
        print("i =", 1, ". j=", j, ". counter =", counter)