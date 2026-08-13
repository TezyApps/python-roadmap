#!/usr/bin/python3

def decide(raining: bool) -> None:
    library_or_beach = "beach" if not raining else "library"
    print("Let's go the", library_or_beach)

for cond in [True, False]:
    decide(cond)