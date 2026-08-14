#!/usr/bin/python3

target = 0

while target < 5:
    print(f"{target}", end=", ")
    target += 1

while target < 0:
    print(f"inside while")
else:
    print("conditon not satisified")

count = 0
while True:
    if count == 5:
        print("limit reached.. exiting while loop")
        break
    count += 1
    print(f"Incrementing count : {count}")