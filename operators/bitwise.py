#!/usr/bin/python3

a,b = 0b10, 0b01

print('\n')
print('-' * 50)
print('Op\t\tSym\t', bin(a), '\t', bin(b))
print('-' * 50)
print('AND\t\t&\t', a & b, "\t", bin(a & b))
print('OR\t\t|\t', a | b, "\t", bin(a | b))
print('XOR\t\t^\t', a ^ b, "\t", bin(a ^ b))
print('NOT\t\t~\t', ~a, "\t", bin(~a), ~b, "\t", bin(~b))
print('L. Shift\t<<\t', a << b, "\t", bin(a << b))
print('R. Shift\t>>\t', a >> b, "\t", bin(a >> b))
print('\n')

# Output:
# --------------------------------------------------
# Op              Sym      0b10    0b1
# --------------------------------------------------
# AND             &        0       0b0
# OR              |        3       0b11
# XOR             ^        3       0b11
# NOT             ~        -3      -0b11 -2        -0b10
# L. Shift        <<       4       0b100
# R. Shift        >>       1       0b1

