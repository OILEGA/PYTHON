# creating a class
class Cristal:
    #attribute
    color = "Blue"

    def __init__(self, id):
        self.id = id
        print("You just created an object")


    #method
    def write(self):
        print("Hey! I am writing")

""" The above is a class that has been created.We are done defining our template.
Based on this template, we can now create our object(a cristal pen) """

""" Instantiation( We now want to create an instance of the class i.e the object) """
"""To do that, we need the name of the class (cristal)and parathesis() and assign it to 
a variable"""

first_pen = Cristal(id='sl-01')

second_pen = Cristal(id='sl-02')

""" How we want to access the method. we want first pen to write . Now we write the name of 
the object and the name of the method which is write."""

#using the method
#first_pen.write()
#second_pen.write()   #anytime we need it to write we call this write method 

#accessing the attribute
print(f" The color of the first pen is {first_pen.color}")
print(f"The ID of the first_pen is {first_pen.id}")
print()
print(f"The color of the second Pen is {second_pen.color}")
print(f"The ID of the second_pen is {second_pen.id}")