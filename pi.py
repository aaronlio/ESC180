# Problem 2
def recursiveAddition(n):
    recursive_total = 0
    for i in range(1, n+1):
        recursive_total += i**3
    return recursive_total

def formulaAddition(n):
    formula_total = 0
    formula_total += int(((n**2)*(n+1)**2)/4)
    return formula_total

def check_sum(n):
    return recursiveAddition(n) == formulaAddition(n)

if __name__ == '__main__':
    print(recursiveAddition(3))
    print(formulaAddition(3))
    print(check_sum(5))

# Problem 3
def Leibniz():
    total = 0
    for i in range(0, 1000):
        total += ((-1)**i)/((2*i)+1)
    return total
    
if __name__ == '__main__':
    print(f"π is about: {Leibniz() * 4}")

