#!/usr/bin/python3

# Logical operators: and | or | not

def calculate_grade(grade: float, has_arrears: bool) -> None:
    gold_medal = grade > 95.0 and has_arrears == False
    distinction = grade > 70.0 and grade < 85.0 and has_arrears == False
    first_class = grade > 50.0 and grade < 75.0 and has_arrears == False
    failed = grade < 50.0 or has_arrears
    passed = grade > 50.0 and not(failed) and not(first_class or distinction or gold_medal) 
    if gold_medal:
        print(f"{grade}\t:\tGold Medalist")
    elif distinction:
        print(f"{grade}\t:\tDistinction")
    elif first_class:
        print(f"{grade}\t:\tFirst Class")
    elif passed:
        print(f"{grade}\t:\tPassed")
    elif failed:
        print(f"{grade}\t:\tFailed")
    else:
        print(f"{grade}\t:\tCan't determine")

grades = [-1, 20, 78, 90, 99]
arrears = [True, True, True, False, False]
for g,a in zip(grades, arrears):
    calculate_grade(g,a)