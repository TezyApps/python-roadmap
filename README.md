# Python Crash Course:

## Basics:
1. [Basics](./basics/hello-world.py)
2. [Python Identifiers](./basics/python-identifiers.py)
3. [Raw Input](./basics/raw-input.py_bkp)
4. [Multi line statements](./basics/multi-line-statements.py)

## Variables:

Python variables are the reserved memory locations used to store values with in a Python Program. This means that when you create a variable you reserve some space in the memory.

Based on the data type of a variable, memory space is allocated to it. Therefore, by assigning different data types to Python variables, you can store integers, decimals or characters in these variables

1. [Intro](./variables/intro.py)
2. [Area_Perimeter](./variables/area_perimeter.py)
3. [Scopes](./variables/scope.py)
4. [public, private, protected variables](./variables/publi_private_protected_variables.py)
5. [Primitive Data types](./variables/data_types.py)
6. [Dictionaries & Sets](./variables/dictionaries_sets.py)
7. [Memory View Use cases](./variables/memory_view_uses.py)
8. [Boolean & None Type](./variables/boolean.py)

<details>
<summary>References</summary>

![public, private & protected varaibles diff](./resources/pub_pvt_protected_vars.png)

| Sr.No. | Function & Description |
|--------|--------------------------|
| 1 | **`int()`** — Converts x to an integer. `base` specifies the base if x is a string. |
| 2 | **`long()`** — Converts x to a long integer. `base` specifies the base if x is a string. This function has been deprecated. |
| 3 | **`float()`** — Converts x to a floating-point number. |
| 4 | **`complex()`** — Creates a complex number. |
| 5 | **`str()`** — Converts object x to a string representation. |
| 6 | **`repr()`** — Converts object x to an expression string. |
| 7 | **`eval()`** — Evaluates a string and returns an object. |
| 8 | **`tuple()`** — Converts s to a tuple. |
| 9 | **`list()`** — Converts s to a list. |
| 10 | **`set()`** — Converts s to a set. |
| 11 | **`dict()`** — Creates a dictionary. d must be a sequence of (key,value) tuples. |
| 12 | **`frozenset()`** — Converts s to a frozen set. |
| 13 | **`chr()`** — Converts an integer to a character. |
| 14 | **`unichr()`** — Converts an integer to a Unicode character. |
| 15 | **`ord()`** — Converts a single character to its integer value. |
| 16 | **`hex()`** — Converts an integer to a hexadecimal string. |
| 17 | **`oct()`** — Converts an integer to an octal string. |

</details>

## Operators:

1. [Arithmetic](./operators/arithmetic.py)
2. [Logical](./operators/logical.py)
3. [Bitwise](./operators/bitwise.py)
4. [Comparison](./operators/comparison.py)
5. [Identity](./operators/identity_ops.py)
6. [Membership Operators](./operators/membership_operators.py)
7. [Ternary Operators](./operators/ternary_operator.py)

### References:
 
 ```py

# Arithmetic:
    +, -, *, /, //, **, %

# Logical:
    and, or, not

# Bitwise:
    &, |, ~, ^, <<, >>

# Comparison:
    ==, !=, >, >=, <, <=

# Identity:
    is, is not

# Membership Operators:
    in, not in

# Ternary operators:
    <statement> if <condition> else <other_statement>
    e.g., `'Drive' if is_green_signal else 'Stop or prepare to Stop'`

```