#<------------------------------------------------------------- Lecture 5 ------------------------------------------------------------>
#<---------- Revisiting the number swap from lecture 2 --------------->
"""Swap the values of a and b, without using a third themporary variable, and without the mutliple assignment trick"""

a = 5
b = 2

a = a + b # a: (old a + old b). b: old b
b = a - b # a: (old a + old b), b: old a
a = a - b # a: old b, b: old a....Done!

# <---------------------- Literals and Booleans ---------------------->
a = True 
b = False # These are boolean values, can be used in conditional statements
a = (5 > 4)

#<---------------- Not, or, and --------------->

not False # True
not True # False

not (1 > 2)

"""A and B is True if both A and B are True, and it's False otherwise"""

True and True #True
False and True #False
True and False #False
False and False # False

(5 == 5) and (2 > 3) #False

"""A or B is True if at least one of A and B is True, False otherwise"""

True or True # True
True or False # True
False or True # True
False or False # False

(1 == 2) or (2 == 3) # True


#<--------------- Replicating the English "or" ----------->
# For dessert, I'll have pie or ice cream
pie = False
ice_cream = True

# Doesn't correspond to the english OR
if pie or ice_cream:
    print("I told the truth")

if (pie and not ice_cream) or (not pie and ice_cream):
    print("I told the truth")

if pie or ice_cream:
    if not (pie and ice_cream):
        print("I told the truth")

if (pie or ice_cream) and not (pie and ice_cream):
    print("I told the truth")

"""These are all ways of saying the same the....but the simpliest way:"""

if pie != ice_cream:
    print("I told the truth")

"""The English "or" is called "exclusive or" whereas the python "or" is inclusive
in Python, the xor exists but it doesn't work the same way on integers... "xor" --> the symbol is ^


Operator precedence for logical/boolean operatures:
Not, then And, then Or
"""


