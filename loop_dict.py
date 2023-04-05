#!/usr/bin/python3

""" Using a for loop to access values in a dictionary """

m_dict = {"mathematics": 98, "science": 80}

for i in m_dict:
    print(m_dict[i])

""" Note that in dictionaries the interest is not in the key but in the value """
""" if we want our interest to be in the key,then er use"""


for i in m_dict.keys():
    print(i)


""" If we want to access the key and value then an item is used to 
be able to print out the keys and values in a tuple form """

for i in m_dict.items():
    print(i)


