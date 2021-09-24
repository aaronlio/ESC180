#<------------------------------ Lecture 7 ------------------------------------>
#< ------------------------------------------------------------------------------------------------>

#<------ Arithmetic Shorthand ------>
""" a += 2 # a = a + 2
a *= 2 # a = a * 12

# 5! = 120
# find the number of trailing zeros in n!

#<------------------ A factorial function + counting the trailing zeros ------------------------>
def fact(n):
    '''Return n!
    n is a positive integer'''
    res = 1
    for i in range(1, n+1):
        res *= i
        
    return res

def trailing_zeros(n):
    fact_n = fact(n)
    counter = 0
    
    # counter = 0
    # fact_n has k trailing zeros

    # each iteration of the while loop:
    #   fact_n has one fewer trailing zeros, counter increments

    # trailing zeros: k, k-1, k-2, .... k, etc
    # counter: 0, 1, 2, 3, ....k
    while fact_n % 10 == 0:
        fact_n //= 10 # fact_n = fact_n / 10, each time we divide by ten, a trailing zero is removed
        counter += 1 # Adds one each time a zero is removed
    
    return counter

if __name__ == '__main__':
    print(trailing_zeros(25))
 """

#< ----------------------------------------------------------------------------------------------------------->
"""This function returns "OK" if username mathes the password, 
unless there were three attempts to call the function with the wrong username/password pair
If the login is not successful (either because username doesn't match password, or because three successive failed logins),
return "Refused"
"""

def login(username, password):
    global n_attempts
    
    if n_attempts >= 3:
        n_attempts += 1
        return "Refused"


    if username == "guerzhoy" and password == "ilovepython":
        n_attempts = 0
        return "OK"
    if username == "stangeby" and password == "rigorous":
        n_attempts = 0
        return "OK"
    if username == "cluett" and password == "matrix":
        n_attempts = 0
        return "OK"
    
    n_attempts += 1
    return "Refused"

def initialize():
    global n_attempts
    n_attempts = 0

if __name__ == '__main__':
    initialize()
    print(login("guerzhoy", "ilovepython"))
    print(login("guerzhoy", "adefefefef"))
    print(login("guerzhoy", "adefefefef"))
    print(login("guerzhoy", "adefefefef"))
    print(login("guerzhoy", "ilovepython"))
    print("\n")
    initialize()
    print(login("guerzhoy", "adefefefef"))
    print(login("guerzhoy", "adefefefef"))
    print(login("guerzhoy", "ilovepython"))
    initialize()


#<------------------ Importing a function from a different file ------------------------>
"""When you're in the working folder, you can import a file using:
import file_name

if there's a function you want to use from the file file_name (ie. initialize),
you can call this function using:

file_name.initialize()

or more generally, 

file_name.function()

From above, we can also do:

print(Lecture7.login("guerzhoy", "ilovepython"))
"""

"""Important note:

When we're importing functions from a different file, the main block from the file whose functions are being imported will not be run,
only the script that you're running will have it main block run. 

Thus, if you're looking to use an initialize function, you can put in above the main block of the imported file so 
it runs as the functions are being read and imported.

"""

def initialize():
    global n_attempts
    n_attempts = 0

initialize() # This can be here because as the initialize function is being imported, initialize will be called as well.
if __name__ == '__main__':
    initialize()


#< ------------------------------------------------------------------------------------------------>

#< -------------------------------- IMPORTANT TOPIC TIME -------------------------------------------------------------------------------------------------------->->

#< --------------------- LISTS -------------------------->

"""Use square brackets to initialize a list"""
earnings = [91, 87, 115, 109]

"""Or use square brackets to index (get a specific value) from a list"""
earnings[0]
earnings[3]

"""Use len(earnings), len is a built-in function, to get the length of the list"""
len(earnings)

for i in range(len(earnings)):
    print(earnings[i])

# To do the same thing as above:

for amount in earnings:
    print(amount)

USD_TO_CAD = 1.25
for amount in earnings:
    amount *= USD_TO_CAD
    print(amount)

for i in range(len(earnings)):
    earnings[i] *= USD_TO_CAD