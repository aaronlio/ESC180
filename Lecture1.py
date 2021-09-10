# <----------------------------------- Basic Intro ------------------------------------------->

""" The simplest operation in python is evaluation"""
x = 3 + 4

""" Strings are a sweies of characters enclosed in double quotes "Hello" """
x = "hello"

""" Operations can include strings """
y = "ha" * 5

""" Variables are used to store values and operations can be conducted on these values. Variable names are not enclosed in quotes. Variables must be declared before they can be used"""
x = 5
y = 10
y = x + y
# print(z) would throw an error because the value of z has not been declared

"""Breakpoints can be used to trace through and debug a program. On VSCode, click beside line number to add a breakpoint"""

examMark = 100
AdjustmentFactor = 10
examMark -= AdjustmentFactor
print(examMark)

    # <------------------------------- Conditional Statements -------------------------------->

"""Conditional statements are statements which test a specific condition. If statements are the most popular conditional statements.
If the condition is true, the statement will be executed. If is a special Python keyword"""
n = 12

if n < 0:
    n = -n
print(n)