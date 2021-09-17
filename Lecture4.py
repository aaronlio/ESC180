#<--------------------------------------------------------- Lecture 4 ---------------------------------------------------------->
#<---------------------  Multiple Assignments -------------------->
a = 5
b = a

a1, a2 = b1, b2
a, b = b, a # a has the old value of b, b has the old value of a

"""Multiple assignment allows you to change variable assignments simultaneously, works for any number of variables.
a, b = b, a
vs:
a = b
b = a ---> both would be equal to b

Another way you could change the variable values is by having a 3rd, temp variable, shown below:
"""

temp = a # temp: old a, a: old a, b: old b
a = b #temp: old a, a: old b, b: old b
b = temp #temp: old a, a: old b, b: old a

""""Let's say that a and b are integers and we want to swap the values, how would you do it?"""

#<------------- Replacing multiple assignments --------------->

b = a + b
a = b - a
b = b - a

#<------------- Data Type Conversions --------------->

"""For data type conversions, ie. from 3.14 --> 3. 
Python conducts truncation when changing data types (be weary of data loss)

You can convert between numerical types, and between string types.
"""

int(3.14) # Truncates to 3
float(3) # = 3.0
str(3.14) # --> 3.14 as a string

approx_pi = 3.14

s1 = "the value of pi is about " + str(approx_pi) # output: the value of pi is about 3.14

float("3.14") # --> 3.14 as a float
int("5") # --> 5 as an int

# Note: you cannot convert directly from float as a string to integer.


"""Like with other dtypes, conversions between booleans are also possible
Anything that's not "" or 0 is True
"""

bool(3.14) # = True
bool("") # = False

""" This is not a particularly useful piece of knowledge, unless you're using the existence of a value (ie. an input) 
in a conditional statement. For example:
"""

if a:
    print("a has a non-zero value!")
#------------------------------------------------------------------------------------------------------------------------------------

#<----------------------- Revisiting Global, Local variables -------------------->
#<---------- Example 1---------->
def adjust_grade2(grade): #grade as a parameter
    grade = grade - 5
    print("new grade inside the function: ", grade)

if __name__ == "__main__":
    grade = 95
    adjust_grade2(grade)
    print("New grade outside the function: ", grade)

"""In the above example, using the parameter, when we change the value of grade within the adjust_grade2 function,
we're not changing the global value. This would only occur if we declared global grade in line 71.
"""

#<---------- Example 2 ---------->
def adjust_grade3(g):
    g = g - 5
    print("new grade inside the function: ", grade)

if __name__ == "__main__":
    grade = 95
    adjust_grade3(grade) # In this statement, grade is an ARGUMENT, and g in line 85 is the PARAMETER
    print("New grade outside the function: ", grade)


"""The variable g is created for the duration of the function execution, g doesn't exist outside of the function (is only
defined within the function).
"""

#<---------- Example 3 ---------->

def adjust_grade4(g):
    global grade 
    grade = g - 5 # The global value of grade changes to 90

if __name__ == "__main__":
    grade = 95
    adjust_grade3(grade)
    print("New grade outside the function: ", grade)

#<---------- Example 4 ---------->
def get_adjusted_grade(grade):
    return grade - 5

if __name__ == "__main__":
    grade = 95
    get_adjusted_grade(grade) # This statement has a value (95 - 5), this by itself has no value, we can set it equal to something tho
    grade = get_adjusted_grade(grade)

#<---------- Example  5---------->
def get_adjusted_grade(grade):
    return grade - 5

if __name__ == "__main__":
    grade = 95
    grade = get_adjusted_grade(grade)# To print this value, we can use a print statement
    print(f"Your grade is {grade}")

#<---------- A common error with variable scope --------->
def grade_error():
    grade = grade - 5 
    print(grade)

if __name__ == "__main__":
    grade = 95 
    grade = grade_error()

"""In this function, grade is undefined locally, we would need to define it, or declare global grade before line 128"""

#<---------- Communicating between main block and function --------->
def minus5(x, y):
    global ret_val_minus5
    ret_val_minus5 = x - 5

if __name__ == "__main__":
    minus5(10, 5)
    print("Result: ", ret_val_minus5)

"""This technically works because ret_val_minus5 is defined as a global variable, though this is not ideal.
Try this instead:
"""

def minus5(x, y):
    return x - y

if __name__ == "__main__":
    res = minus5(1, 2)

"""Using this (return value) format, we're able to set the return equal to a variable."""

