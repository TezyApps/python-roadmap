#!/usr/bin/python3

data = bytearray(b'hello')
print(data)

# Without memory view
chunk = data[0:5]   # new bytearray object, separate memory
chunk[0] = ord('H') # what does this ord() function do?
print(f"Original Data\t\t${data}")
print(f"Copied Data\t\t${chunk}")
print(f"Copy's first char\t${chunk[0]}")

# for char in ['A', 'a', 'B', 'b', 'Z', 'z']:
#     print(("Unicode " + char + " = "), ord(char))

#With memory view
mv = memoryview(data)
m_chunk = mv[0:5]
m_chunk[0] = ord('H')
print(data) # modified the original data