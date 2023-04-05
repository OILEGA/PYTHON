#!/usr/bin/python3
""" In turples you cannot append or delete items from it.
but it is possible to create a new turple and concatenate two turples to it"""
scores = (80, 56, 85, 90)
for score in scores:
    print(scores)
num = (40,25, 16)

new_score = scores + num
for score in new_score:
    print(score)