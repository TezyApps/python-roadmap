#!/usr/bin/python3

a = True
b = False
eval_a = bool(a)
print(a, eval_a, b, bool(b))
print(f'a : {a} == b: {b} => bool(a==b) {bool(a==b)} (or simply) a == b {a == b}')

# Other data types, empties, none, etc.
text_empty=""
text_non_empty="Hello"
print("Empty text", text_empty, bool(text_empty))
print("Non-Empty text", text_non_empty, bool(text_non_empty))

empty_tuple = ()
print("Empty tuple", empty_tuple, bool(empty_tuple))

non_empty_tuple = (1,2)
print("Non Empty tuple", non_empty_tuple, bool(non_empty_tuple))

val = 0
print(val, bool(val))

val = 12
print(val, bool(val))

none_type = None
print("None type", none_type, bool(none_type))