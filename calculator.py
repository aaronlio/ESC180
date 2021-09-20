# Problem 1
""" if __name__ == '__main__':
    current_value = 0
    print(f"Welcome to the Calculator Program\n Current value: {current_value}") """

# Problem 2
""" def display_current_value():
    print(f"Current value: {current_value}")

if __name__ == '__main__':
    current_value = 0
    display_current_value() """

# Problem 3 & 4
""" def display_current_value():
    print(f"Current value: {current_value}")

def add(to_add):
    global current_value # Problem 4 addition
    current_value += to_add
    return current_value


if __name__ == '__main__':
    current_value = 0
    display_current_value()
    add(5)
    display_current_value() """

# Problem 5
def display_current_value():
    print(f"Current value: {current_value}")

def add(to_add):
    global current_value # Problem 4 addition
    current_value += to_add
    return current_value

def multiply(to_multiply):
    global current_value
    current_value *= to_multiply
    return current_value

def divide(to_divide):
    global current_value
    current_value //= to_divide
    return current_value
    # This could've posed a problem if we used non-integer division because it would return a float instead of an integer

def memory(to_save):
    global saved_value
    saved_value = to_save
    return saved_value

def recall(to_recall):
    print(f"Saved value: {saved_value}")

if __name__ == '__main__':
    saved_value = 0
    current_value = 0
    display_current_value()
    add(5)
    display_current_value() 
    divide(5)
    memory(current_value)
    display_current_value()
    multiply(10)
    display_current_value()
    recall(saved_value)