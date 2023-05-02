#Exercise 8_1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

alist = [1, 2, 3, 4, 5, 6]

def chop(t):
    del t[0]
    del t[-1]
    return None

def middle(t):
    return t[:]

print (chop(alist))

print (middle(alist))