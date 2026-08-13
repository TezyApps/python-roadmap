#!/usr/bin/python3

x, y, z = 10, 20, [1,2,3,4,5,6,7,8,9,10,11,12]

print(f"x: {x}\ny: {y}\nz: {z}")

def membership_ops(x, y, z):
    if (x in z):
        print(f"x: {x} is present in {z}")
    else:
        print(f"x: {x} is not present in {z}")

    if (y not in z):
        print(f"y: {y} is not present in {z}")
    else:
        print(f"y: {y} is present in {z}")

membership_ops(x,y,z)

a = int((x + y) / 4)
membership_ops(a, y, z)