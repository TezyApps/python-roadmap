#!/usr/bin/python3

# how to make this reusable
def log_title(title: str) -> None:
    count = title.__len__()
    line = "=" * (count + 2)
    print("\n ", title, "\n", line, "\n")

def the_end() -> None:
    print("\n", "*" * (30), "\n")

# 1. Basic data types - int, boolean, float, complex, string
log_title('1. Basic data types - int, boolean, float, complex, string')
day = 1
isValid = True
pi = 3.14
complex_number = 10+3j 

# 1a. string
# log_title('1a. string')
text_single_quotes = 'Hello'
text_double_quotes = "World"
text_tripe_single_quotes = '''
Hello World. this is multi-
line string.
'''
text_tripe_double_quotes = """
Hello World. this is multi-
line string.
"""

# 1b. String operations - slicing, concatenation
# log_title('1b. String operations - slicing, concatenation')

text_ops = "Texts Operations"
print(text_ops)

first_char = text_ops[0]
first_char_type = type(first_char)
print(first_char_type, " = ", first_char)

text_range = "0123456789"
text_range_2_to_5 = text_range[4:5] # range - [starting_index : end_index]
text_range_2_to_5_type = type(text_range_2_to_5)
print(text_range_2_to_5_type, " = ", text_range_2_to_5)

text_from_3 = text_ops[3:]
print("Text from 3rd char ", text_from_3)

text_repeating_twice = text_ops * 2
print(text_repeating_twice)

text_concatenated = text_ops + " * 2 = " + text_repeating_twice
print(text_concatenated)

# 2. Sequence data types - list, tuple, range

log_title('2. Sequence data types - list, tuple, range')

# ![IMPORTANT]: Python lists are heterogenous array 
#   - means, it can hold different data types in the array
#   - also, it can have nested other data types as well.

list_same_data_types = [1,2,3,4,5]
print(list_same_data_types)

list_different_data_types = [2023, "May", 20, "Wednesday", "10:30 AM"]
print(list_different_data_types)

nested_list = [list_same_data_types, list_different_data_types, [True, False], "Hello again"]
print(nested_list)

# 2a. List Operations:
print("First item in the list", list_same_data_types[0])
print("Items : 0 to 3", list_different_data_types[0:3]) # predicting: [0: 2023, 1: "May", 2: 20] and not the 3rd index [3: "Wednesday"]
print("Items: from 2nd index", list_same_data_types[2:])
print("Items * 2", list_same_data_types * 2)
print("Concat list", list_same_data_types + list_different_data_types)

# 3a. Tuple data type
tuple_data_intro = "3a. Tuple data type"
log_title(tuple_data_intro)

# A tuple is also a sequence, hence each item in the tuple has an index referring to its position in the collection. The index starts from 0.

# ![IMPORTANT]:
# The main differences between lists and tuples are: 
#   - Lists are enclosed in brackets ( [ ] ) and their 
#     elements and size can be changed i.e. lists are mutable, 
#   - while tuples are enclosed in parentheses ( ( ) ) and cannot be updated
#     (immutable). Tuples can be thought of as read-only lists.

tuple_data = (13, "Aug", 2026, "12:45 PM")
print(tuple_data)
print("Index 0 :", tuple_data[0])
print("Slicing [0:2]", tuple_data[0:2])
print("good to know", tuple_data[-1])
# print("what this does? let's try", tuple_data[-5]) # IndexError: tuple index out of range

# 4a. Range Data Type
log_title('4a. Range Data Type')

# syntax: range(start, stop, step)
#   - start : starting position index. 
#               [Optional, default: 0]
#   - stop  : ending positition index. 
#               [Mandatory]
#   - step  : incremental number.
#               [Optional, default: 1]

for i in range(3):
    print("Inside range(3), position :", i)

print("\n")

for i in range(0, 10, 2):
    print('range(0, 10, 2) =>', i)

print("\n")

# 5a. Bytes data type
log_title('5a. Bytes data type')

# 3 ways to represent binary data
#   a. bytes: 
#       The byte data type in Python represents a sequence of bytes. 
#       Each byte is an integer value between 0 and 255. 
#       It is commonly used to store binary data, 
#       such as images, files, or network packets.
#
#   b. bytearray
#   c. memoryview
#       In Python, a `memoryview` is a built-in object 
#       that provides a view into the memory of the original object, 
#       generally objects that support the buffer protocol, 
#       such as byte arrays (bytearray) and bytes (bytes). 
#       It allows you to access the underlying data of the 
#       original object without copying it, providing efficient 
#       memory access for large datasets.

bytes_example = bytes([65, 66, 67, 68, 69])
print("Bytes : ", bytes_example) # outputs: b'ABCDE'

# another way of declaring bytes by prefixing b'<text goes here>'
bytes_hello = b'Hello'
print(bytes_hello)

bytes_array_example = bytearray([72, 101, 108, 108, 111])
print(bytes_array_example) # outputs: bytearray(b'Hello')

# another example with encoding: utf-8
bytes_array_example_2 = bytearray('hello', 'utf-8')
print(bytes_array_example_2) # outputs: bytearray(b'hello')

# memory view
bytes_example_memory_view = memoryview(bytes_example)
print(bytes_example_memory_view, id(bytes_example_memory_view))

import array
arr = array.array('i', [1,2,3,4,5])
amv = memoryview(arr)
print(amv)

the_end()