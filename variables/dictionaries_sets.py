#!/usr/bin/python3

# 1. Dictionaries

dict_example = { 
    'month': 'Aug',
    'day': 'Wednesday',
    'year': '2026'
}
print(dict_example)

print(dict_example['month'])
print(dict_example['day'])

# for unknown keys:
#     Traceback (most recent call last):
#       File "/Users/vengat/Source/personal/my-projects/learning-path/agentic-ai/python/variables/./dictionaries.py", line 14, in <module>
#       print(dict_example['date'])
#       KeyError: 'date'
# print(dict_example['date'])

# 1b. Defered assignment:
lookup = {}
lookup[1] = 'One'
lookup[2] = 'Two'
lookup['3'] = 'Three'
print(lookup)

# Can't use for loop to iterate dictionary?
# for (k, v) in lookup:
#     print(f"key: {k}, value: {v}")

# Error:
# Traceback (most recent call last):
#   File "/Users/vengat/Source/personal/my-projects/learning-path/agentic-ai/python/variables/./dictionaries.py", line 29, in <module>
#     for (k, v) in lookup:
# TypeError: cannot unpack non-iterable int object

for key in lookup.keys():
    print(f"Key: {key},\tValue: {lookup[key]}")

# 2. Sets

# Sets > collection of unique elements
#   can store only immutable objects, e.g.,: int, float, bool, str, tuple (which are hashable)
#   can't have mutable objects inside it. eg., list, dict (not hashable) 

sets_example = { 2023, 2024, 'Python', 1+2j, '/bin', (1,2), True, False, True }
print(type(sets_example), sets_example)