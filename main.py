# This is a sample Python script Based on CH.3 material
# ASCII text generated with http://www.network-science.de/ascii/
# Donte Jones jones_donte@dublinschools.net
# IT Academy @ Emerald Campus
#
# Notes PYCHARM users: Use CTRL+/ to uncomment or comment any selected lines of code



import random

"""
OOP 
Object Oriented Programming - Classes 

OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them.
This approach to programming is well-suited for programs that are large, complex and actively updated or maintained.

Software Objects allow you to model software objects around real world objects
Creating objects starts with creating CLasses 
"""
#
# # Simple Critter
# # Demonstrates a basic class and object
#
# class Critter(object): # Creates the class object
#     """A virtual pet""" # Doc string - *Optional
#     def talk(self): # Class method
#                     # 'self' parameter is required it represents the particular instance of the object
#         print("Hi.  I'm an instance of class Critter.")
#
# # main
# crit = Critter() # Creates an instance object (instantiates) from the class Critter named 'crit'
# crit.talk() # Every Class object inherits methods defined by the class
#             # Class methods are accessed through the dot notation
#
# input("\n\nPress the enter key to exit.")




"""
CONSTRUCTORS 

Constructors are special methods of a class used to setup initial values of an object
This method is called automatically after an object is created
"""
# # Example 1
# # Constructor Critter
# # Demonstrates constructors
#
# class Critter(object): # Class definition
#     """A virtual pet"""  # Doc string
#     def __init__(self):  # Builtin method recognized by Python and run on object creation
#         print("A new critter has been born!")
#
#     def talk(self):
#         print("\nHi.  I'm an instance of class Critter.")
#
# # main
# crit1 = Critter()
# crit2 = Critter()
#
# crit1.talk()
# crit2.talk()
#
# input("\n\nPress the enter key to exit.")


"""
Here we are creating Objects that have class attributes (variables) and class methods (functions) 
"""


# Example 2
# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name

    def __str__(self):                      # Added a String method using builtin Python function
        rep = "Critter object\n"            # Function returns a specified string when the object
        rep += "name: " + self.name + "\n"  # is printed
        return rep

    def talk(self):
        print("Hi.  I'm", self.name, "\n")




class MysteryCritter(object):
    """A virtual pet of some type"""
    def __init__(self, name):
        print("A new mysterious critter has been born!")
        self.name = name


    def talk(self):
        print("Hi. I'm,", self.name, "\n")


# main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

crit3 = MysteryCritter("Chad")
crit3.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)  # Directly accessing variables of the object

print("\nPrinting crit3:")
print(crit3)

input("\n\nPress the enter key to exit.")



"""
CLASS ATTRIBUTES & STATIC METHODS 

Class attributes allow you to create a single value associated with the class for example 
this would be similar to a post-it stuck to a blueprint. Only one copy exists no matter how
many houses are built from the plans. 


"""


# Classy Critter
# Demonstrates class attributes and static methods

class Critter(object):
    """A virtual pet"""
    total = 0       # Class attribute *(Assigned outside of all class methods)
                    # Exists even before any objects are created

    @staticmethod   # Method decorator, Method exists for the class NOT for objects
    def status():   # Notice 'self' is not a parameter here
        print("\nThe total number of critters is", Critter.total)
                                                                    # class attributes are NOT invoked through objects
    def __init__(self, name):  # Constructor Method
        print("A critter has been born!")
        self.name = name
        Critter.total += 1 # Class attribute is incremented each time a critter is created
                           # Remember the __init__ method is called automatically with object creation

# main
print("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)    # Accessing the class attribute before any objects exist

print("\nCreating critters.")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status()