# <----------------------------------- Lecture 2, Conditionals and Functions ------------------------------------------->

# <--------------------- The Big Picture ------------------------>

"""A program is a sequence of instructions to the computer, 
some programs are written in machine language, which is directly executed by electronics.

ie. "Change cell 20040 to 1"

Most programs are not written in machine language, we use letters/words instead of issuing instructions pixel-by-pixel
"""

#<------------------ Python: a scripting language --------------->
"""Python is a human-like language, where we issue instructions at a higher level of abstraction than the machine language.
Another program, called a Python Interpreter, takes Python files/commands and executes them.
"""

#<----------- Pyzo ------------>
"""An Integrated Development Environment (IDE), which allows us to write python programs and execute them. 
Also runs the script line by line so we can see where the errors are (debug). 
"""

# Note: In ESC180, practice problems and understanding a given solution's approach is more useful than reading a textbook.

# <--------------------------------- Code Time! ------------------------------>

# <------ Fun Intro: Secret Number game ------>

secret_num = 20
temp = secret_num + 8
temp = temp / 4
answer = temp - secret_num / 2
#print(answer)

#<-------- More about Conditionals ------->
"""Remember from last lecture, conditional statements are executed if the condition is true. 
If it isn't, the statement will be skipped. Conditional statements are indented (called a code block)
"""

exam_grade = 99
if exam_grade == 98:
    print("I won the bet, I'm happy")
elif exam_grade > 98:
    print("I'm happy")
else:
    print(":-(")

#print("At least I'm not an artscie")

# The Jack Sparrow Example: https://nbviewer.jupyter.org/github/guerzh/esc180lec/blob/master/week1/ConditionalPirates.ipynb"
shillings = 2
name = "Jack Sparrow"

if shillings >= 3:
    print("Welcome to Port Royal, Mr. Smith")
elif shillings >= 1:
    print("Welcome to Port Royal, " + name)
else:
    print("Go away please")

"""In this previous code block, each of the conditions are read, when a TRUE condition is encountered (ie. 3 >= 2),
none of the following conditions are evaluated. 
In the following example, there is no way to get the elif block (2nd condition to run)
"""

# <-------------- A buggy Jack Sparrow Example ------------ >
shillings = 3
name = "Jack Sparrow"

if shillings >= 1:
    print("Welcome to Port Royal, " + name)
elif shillings >= 3:
    print("Welcome to Port Royal, Mr. Smith")
else:
    print("Go away please")
#print("It was a pleasure serving you")

"""Since 3 is >= 1, the if block will be executed, but the elif block won't be (even though 3 >= 3), 
since it comes after the if statement. You can use multiple IF statements, instead of elif, 
if you don't want them to be automatically skipped if a previous condition is true. See Below
"""

shillings = 300000001
name = "Jack Sparrow"

if shillings >= 300000000:
    print("Welcome to Port Royal, Mr. Smith. Here is your iron ring")
if shillings >= 3:
    print("Welcome to Port Royal, Mr. Smith")

"""Both if statements will be evaluated: printing 
"Welcome to Port Royal, Mr. Smith. Here is your iron ring
Welcome to Port Royal, Mr. Smith"
"""

# <------------- Multiple ELIFS ------------>
shillings = 300000001
name = "Jack Sparrow"

if shillings >= 300000000:
    print("Welcome to Port Royal, Mr. Smith. Here is your iron ring")
elif shillings >= 3:
    print("Welcome to Port Royal, Mr. Smith")
elif shillings >= 1:
    print("Welcome to Port Royal, " + name)
else:
    print("Go away please")

"""This will print "Welcome to Port Royal, Mr. Smith. Here is your iron ring" """


# <--------- Writing reusable code ---------->
shillings = -.5
name = "Jack Sparrow"
welcome_message = "Welcome to Port Royal"
if shillings >= 3:
    name = "Mr. Smith"
elif shillings < 1:             #Could say if shillings < 1 -- why?
    welcome_message = "Go away"
#print(welcome_message + ", " + name)

"Using welcome_message means we don't have to change multiple lines"


# <-------------------------------- Quadratic Calculator -------------------------------->
# We want to compute the roots of the equation
# ax^2 + bx + c
import math # A library that will allow us to use sqrt

a = 1 # Cannot be zero
b = 2
c = 5

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    r1 = (-b + math.sqrt(discriminant)) / ( 2 * a)
    r2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(r1, r2, sep = ", ")

elif discriminant == 0:
    r = -b / (2 * a)
    print(r)

else:
    print("No real roots :-(")

# <----------------------- Functions !!!!! VERY IMPORTANT -------------------->

# In math" f(x) = x^2
def f(x):
    return x*x

"""def is the function declaration keyword, the format is 

def function_name(input_values):
    what the function does 
    
"""

def my_add(a, b):
    result = a + b
    print("When printed from inside the function, result is: ", result)
    return result

print(my_add(5, 2) * 10) 
# This line calls my_add, setting a = 5, and b = 2 as inputs for my_add, then multiplies result by 10, will output 70
""" In order for a function to do something, we need to call it (not just define it)

Line 166 is an example of calling the function, we could also just do:
"""

my_add(1, 2) # or
print(my_add(5, 6))

