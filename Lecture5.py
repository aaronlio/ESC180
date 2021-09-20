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
in Python, the xor exists but it doesn't work the same way on integers... "xor"
"""


#<--------------- Operator Precedent ------------->
lazy = False 
smart = True
growthmindset = True

if not lazy and smart and growthmindset:
    print("EngSci")
elif lazy and smart:
    print("Physics")
elif not lazy and smart and not growthmindset:
    print("Econ")
else:
    print ("Ryerson")

#<-------------------- Has roots function example using operator precedent -------------------->
def has_roots(a, b, c):
    '''Return True iff ax^2+bx+c has at least one real root'''
    return b**2 -4*a*c >= 0

def has_no_roots(a, b, c):
    return b**2 -4*a*c < 0

def has_no_roots2(a, b, c):
    return not has_roots(a, b, c)

if __name__ == '__main__':
    print(has_no_roots2(1, 2, 3))


#<-------------------------------->

""" def artsie_math(arg1, arg2, op):
    '''Return arg1 op arg2, where arg1 and arg2 are numbers and op is on of "+" or "-",
    if op is neither "+" nor "-", print an error message'''
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    else:
        print("I am an artsie, I don't know ops that are not + or -")
        # The return here is none


if __name__ == '__main__':
    #print(artsie_math(4, 5, "+"))
    print(artsie_math(4, 5, "*")) # Since this function will not have any return with these arguments, it defaults to None """

#<------------ A better version of the last function ------------->
def artsie_math(arg1, arg2, op):
    if op != "+" and op != "-":
        return None

    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2

if __name__ == '__main__':
    res = artsie_math(4, 5, "*")
    if res != None:
        print(res)
    else:
        print("The artsie had a hard time")
