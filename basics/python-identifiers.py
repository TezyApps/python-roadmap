#!/usr/bin/python3

# Lesson 2: Python Identifiers
"""
A Python identifier is a name to identify 'variable, function, class, module or other object'.

Conventions:

1. Class names starts with Uppercase letters, rest all starts with lower case letters.
2. starting with _ indicates it's private identifier.
3. starting with __ indicates it's strongly type private identifier. [claude] - what's strongly type private identifier?
4. starts and ends with __, then it's a language-denfined special name. [claude] - what are other examples?

Reserved keywords:
and | as | assert
break | class | continue
def | del | elif
else | except | False
finally | for | from
global | if | import
in | is | lambda
None | nonlocal | not
or | pass | raise
return | True | try
while | with | yield
"""

# Python Lines and indentations
"""
1. has no braces for block of code > class, functions or flow control.
2. only 'line indentation' rigidly enforced.
"""
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")

# Python Multi-Line statements:
total = "1" + \
    "2" + \
    "3"
print(total)

