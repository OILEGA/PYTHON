#!/usr/bin/python3

""" To generate the squares of the members of a given list using a for loop"""
nums = [1, 2, 3, 4]
new_nums = []

#using a for loop to loop thru the numbers and square them

for num in nums:
    new_nums.append(num ** 2)

print(f'nums: {nums}')
print(f"new_nums: {new_nums}")


# using the list comprehension method
compr_num = [num ** 2 for num in nums]
print (f"compr_num : {compr_num}")