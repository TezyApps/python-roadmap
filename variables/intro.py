#!/usr/bin/python3

# Common Datatypes:
#   1. str
#   2. int
#   3. float
#
# Naming Convention:
#   - A variable name must start with a letter or the underscore character
#   - A variable name cannot start with a number or any special character like $, (, * % etc.
#   - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#   - Python variable names are case-sensitive which means Name and NAME are two different variables in Python.
#   - Python reserved keywords cannot be used naming the variable.
#
#   - Camel case − First letter is a lowercase, but first letter of each subsequent word is in uppercase. For example: kmPerHour, pricePerLitre
#   - Pascal case − First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre
#   - Snake case − Use single underscore (_) character to separate words. For example: km_per_hour, price_per_litre

# 1. Getting the memory address of a variable | where is the variable stored?
month = "May"
month_address_loc = id(month)
print("Address for month", month_address_loc)
print("-")

age = 18
age_address_loc = id(age)
print("Address for age", age_address_loc)

# Integer Variable
counter = 100
print(counter)

# Float variable
miles = 10.0
print(miles)

# string variable
name = "Hello Python"
print(name)

# Deleting python variables
# del var1[,var2,[,var3[...,varN]]]
del counter

# print(counter) 👇
# Traceback (most recent call last):
#   File "/Users/vengat/Source/personal/my-projects/learning-path/agentic-ai/python/variables/./intro.py", line 27, in <module>
#     print(counter)
# NameError: name 'counter' is not defined

# Getting the type of a variable
# syntax: type(var1)
counter = 10    
print(type(counter))        # <class 'int'>

name = "Vengat"
print(type(name))           # <class 'str'>

float_var = 10.0        
print(type(float_var))      # <class 'float'>

# is this a type in python?
double_var = 10.000         # this is also a float
print(type(double_var))     # <class 'float'>

# Casting python variables:
x = str(counter)
print("counter ", type(counter), "=>", x, type(x))
y = int(float_var)
print("float_var ", type(float_var), "=>", y, type(y))
z = float(counter)
print("counter ", type(counter), "=>", z, type(z))

# Multiple assignment:
a=10
b=10
c=10
print(a, b, c)

# option 2: shorthand in same line for same value
a=b=c=20
print(a,b,c)

# option 3: shorthand in same line for different values
a,b,c = 10, 20, 30
print(a,b,c)