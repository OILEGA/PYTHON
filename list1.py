#!/usr/bin/python3

scores = [79, 68, 98, 55]

for score in scores:
    # for any score less than 90, add 10 marks
    print(f"Before: {score}")
    if score < 90:
        score = score + 10
    print(f"After: {score}")