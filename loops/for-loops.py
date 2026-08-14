#!/usr/bin/python3

# Types of for loop in python

# looping string array
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color, end=", ")

# looping tuple array
points = [(1,4), (3,5), (7,2)]
for x, y in points:
    print(f"x : {x}, y: {y}")

# looping int array
numbers = [1,2,3,4,5]
squared = []
for number in numbers:
    s = number * number
    squared.append(s)

print(f"{squared}")

# looping built-in sequences
bio = ("TezyApps", "iOS/macOS platform engineer", 2026)
for field in bio:
    print(field, end=", ")

print()

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in text:
    print(char.lower(), end=", ")

print()

for i in range(1, 5, 1):
    print(i, end=", ")

# looping dictionaries

students = { 
    "Alpha": 90.0,
    "Beta": 45.0,
    "Charlie": 85.0,
    "Delta": 23.0,
    "Echo": 98.0
}
print()
for student in students: # default, it's keys only in python
    print(f"{student}: {students[student]}", end=", ")
print()
for student_name in students.keys(): # explicit key loops
    print(student_name, end=", ")
print()
for mark in students.values(): # explicit value loops
    print(mark, end=", ")
print()

# looping both key and value : .items() pythonic way
title = " Name\t| Score"
print(title)
print("=" * (len(title) + 6))
for name, mark in students.items():
    print(f"{name}\t: {mark}")

# Advanced looping syntax:

# break

def break_example():
    for n in range(5):
        print("Evaluating", n)
        if n == 3:
            print("Target Found", 3)
            break
    print('break_example: this line executes')

break_example()

def continue_example():
    for i in range(6):
        print("Eval", i, end=" | ")
        if i % 2 == 0:
            print(f'{i} : Skipping evens…')
            continue
        print(f'{i} : Odd')
    print('continue_example: this line executes')

continue_example()

# def continue_example_simplified():
#     for i in range(6):
#         print("Eval", i, end=" | ")
#         continue if i % 2 != 0 else "skip"
#         print(result)
#     print('continue_example: this line executes')

# continue_example_simplified()

def for_with_else_clause():
    for i in range(5):
        print(i, end=" > ")
        if i == 9:
            print(f"Target found: {i}")
    else:
        print(f"Target not found in the list…")

for_with_else_clause()

# for loop and indices
def for_loop_by_indices():
    vals = [1,2,3,4,5]
    indices = len(vals)
    for i in range(indices):
        print(f"vals[{i}] = {vals[i]}")

for_loop_by_indices()

# for loop by built-in enumerate() fn.

def for_loop_enumerate_items():
    for (index, number) in enumerate(range(5)):
        print(f"Index: {index}, Number: {number}")

for_loop_enumerate_items()

# for loop by built-in enumerate(options, start) fn.

def for_loop_enumerate_items_with_options():
    for (index, menu) in enumerate(["open", "save", "settings", "quit"], start=1):
        print(f"{index}. {menu}")

for_loop_enumerate_items_with_options()

# zip()
def for_loop_with_zip():
    indices = ['a', 'b', 'c']
    answers = ["Yes", "No", "May Be"]

    for index, answer in zip(indices, answers):
        print(f"{index}) {answer}")

for_loop_with_zip()

# chain()
from itertools import chain
def for_loop_with_chain():
    r1 = range(1,3)
    r2 = range(4, 8, 2)
    for val in chain(r1, r2):
        print(f"{val} ^ 2 = {val * val}")

for_loop_with_chain()