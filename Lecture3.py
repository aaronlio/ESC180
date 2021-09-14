#<----------------------------- Lecture 3 ------------------------>
#<-------------- Booleans ------------->

# The built-in function "type(variable)" tells us the data-type of a given variable
a = 5
b = 3.4

"""type(a) will return int, type(b) will return float, type("Hello") will return str

Another important data type is bool, or boolean. In essence, a boolean is True or False.
"""

1 == 1 #Returns the boolean value "True"
1 == 2 # Returns the boolean value "False"

"""Conditional statements also evaluate as bools. The below example shows that a > 4 evaluates
to True, which is why the statement is exectured"""

if a > 4:
    print("Hi")

a_greater_than_4 = (a > 4) #Storing bool value "True" in a variable
if a_greater_than_4: #Same as if a > 4
    print("Hi")


#------------------------------------------------------------------------------------------------------------------------#


#<-------------- String Literals ---------------->
"""String literals are an important part of python, if you want to use quotes you have two options: 
single/double quotes, or escape characters"""

"Artsies are "smart"" # invalid
"Artsies are 'smart'" # Valid
"Artsies are \"smart\"" # The escape character \ will allows the double quotes to appear in the string. 
"Artsies are \\smart\\" # How to get a forward slash using escape characters

"""To have multi-line strings, use triple single quotes or the \n escape character"""

a = '''one line
two line'''

b = "one line\ntwo line"

#------------------------------------------------------------------------------------------------------------------------#

#<------------------Arithmatic--------------->
type(2 + 5) #7, returns int
type(5 / 2) # 2.5, returns float
type(4 / 2) # 2.0, returns float 
type(4 // 2) # 2, type int - Called integer division
type(7 // 3) # 2, type int - Effectively floors the value *but not really*
type(7 // -2) # -4, type int, ^
type(2 * (7 // 2)) # 6, 7 // 2 = 3, 2 * 3 = 6, type int


#<------------- More About Functions  ------------->
def f(x):
    '''Return the square of the input x
    '''
    return x**2

"""The reason we use the string in f(x) is so if we enter help(f) or f(x) in terminal, it will output
the string, useful as a description


There's a difference between a return function and a non-return/built-in function.

a = f(10) will set a to 10
a = print(10) will not set a to anything --> will be type None
"""

#<------- Example of a bad function ------>
def pirate_print(s):
    '''Priint the piratified version of s'''
    print("Ahoy! " + s + " Yarr!")
    # This is not an ideal way of defining a function, we'd rather separate the computation and output


#<---------- A good function --------->
def pirate_transform(s):
    '''Return the piratified version of the string s'''
    return "Ahoy! " + s + " Yarr!"

a = pirate_transform("CIV")
print(a) # Separates return from computation


pirate_transform(pirate_transform("Calc")) # Returns "Ahoy! Ahoy! Calc Yarr! Yarr!,"

def has_roots(a, b, c):
    '''Return True iff ax^2+bx+c has at least one real root [otherwise return False]'''
    disc = b**2 - 4* a * c
    # if disc >= 0:
    #   return True
    # else:
    #   return False
    return disc >= 0

print(has_roots(1, 2, 1)) # Since disc >= 0, will return AND print True with these values

"""Inputs of a function, as well as variables stored within a function (ie. 1, 2, 1 above), exists only
within the scope of the function/while the function is running.

This is a VERY important concept, referred to as LOCAL VARIABLES
"""

#------------------------------------------------------------------------------------------------------------------------#
#<-------------- if __name__ == '__main__': block ----------------->
"""After we define all of our function, like has_roots and pirate_transform above,
we must create the main program that will actually call the functions. 

Read more about why we use this block: https://stackoverflow.com/questions/419163/what-does-if-name-main-do

"""

#<--------- Example of global/local variables -------->
def f(x):
    x = 100
    y = 5
    return x ** 2 # x is a local variable here

if __name__ == '__main__':
    x = 15 # x is a global variable here
    res = f(5)
    print(res)
    print(x) # Will return the global x.
    print(y) # This line will return an error, y only exists as a local variable in f(x).



"""
Here's what happens to x and res:
    
    The global x is 15, since we set it in line 125
    The local x is set to 5 when we enter f(5) in line 126
    This local x has its value changed to 100 in line 120

    The global res value uses the local variable x = 100, so res == 10000
    The local variable y, defined in 121, is not defined outside f(x), so we cannot see it outside the function

"""


#<--------- Another Example of global/local variables -------->

def plunder_grade():
    grade = 79

def actually_plunder_grade():
    global grade #importing the global grade means that the value will be changed globally
    grade = 79

if __name__ == '__main__':
    grade = 97
    plunder_grade()
    print(grade) # This will print 97 because the changed value of 79 only exists inside plunder_grade()
    actually_plunder_grade()
    print(grade) # Will print the changed value of 79.
