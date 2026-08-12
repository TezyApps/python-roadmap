#!/usr/bin/python3

# Defining 'private' variables
#       prefix with double underscore __

class PrivateVariablesExample:

    def __init__(self) -> None:
        self.__private_var = "I'm a private variable"

    def show_private_var(self):
        return self.__private_var

obj = PrivateVariablesExample()
# print(obj.__private_var)        # compile time OK; runtime -> error
#       Traceback (most recent call last):
#         File "/Users/vengat/Source/personal/my-projects/learning-path/agentic-ai/python/variables/./private_variables.py", line 15, in <module>
#           print(obj.__private_var)        # compile time OK; runtime -> error
#       AttributeError: 'PrivateVariablesExample' object has no attribute '__private_var'
print(obj.show_private_var())     # Correct usage

# ![IMPORTANT]: Name Mangling for Private Variables
#   - In Python, private variables are not truly private. 
#   - They can still be accessed from outside the class using a technique called name mangling. 
#   - That is, when you create a private variable using a double underscore (__var), 
#   - Python internally changes its name to _ClassName__var. 
#   - Now, you can access the private variable using this mangled name. 

# Example: Access private var using name mangling technique
# print(obj._PrivateVariablesExample__private_var) # Doesn't work? why?

# Private Methods in Python:

class PrivateMethodExample:
    def __init__(self) -> None:
        self.__private_var = "I'm a pvt var"

    def __private_method(self):
        return "I'm a private method"

    def show_private_var(self):
        return self.__private_var

    def call_pvt_method(self):
        return self.__private_method()

obj = PrivateMethodExample()
print(obj.call_pvt_method())