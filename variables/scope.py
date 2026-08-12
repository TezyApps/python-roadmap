#!/usr/bin/python3

# Python Local Variables 
#   Are defined inside a function. 
#   We can not access variable outside the function.

def sum(x, y):
    sum = x + y
    return sum

print("sum: 14 + 28 = ", sum(14, 28))

# Python Global variables
x, y = 14, 28
def mul():
    mul = x * y
    return mul

print("mul:", x, "*", y, "=", mul())

# Note:
# Constants in Python:
# Python doesn't have any formally defined constants. 
# However you can indicate a variable to be treated as a constant by using all-caps names with underscores.
# For example, the name PI_VALUE indicates that you don't want the variable redefined or changed in any way.