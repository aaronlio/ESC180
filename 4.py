""" # Problem 1
def count_evens(L):
    evens = 0
    for num in L:
        evens += 1

# Problem 2
def list_to_str(lis):
    for num in lis:
        print(str(num), end = ' ')
    
    print("")

if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5]
    list_to_str(lis) """

# Problem 3
""" def lists_are_the_same(list1, list2):
    for i in range(0, len(list1)):
        if list1[i] == list2[i]:
            pass
        else:
            return False
            break
    
    return True 
    
    
if __name__ == '__main__':
    lis1 = [1, 2, 3, 4]
    lis2 = [1, 2, 3, 4, 5]
    print(lists_are_the_same(lis1, lis2))"""

# Problem 4
def simplify_fraction(n, m):
    for i in range(1, n, -1):
        print(i)
        if n % i == 0 and m % i == 0:
            print(n)


            
if __name__ == '__main__':
    for i in range(1, 10, -1):
        print(i)
    simplify_fraction(16, 8)