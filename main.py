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

# Simple Critter
# Demonstrates a basic class and object

class Critter(object): # Creates the class object
    """A virtual pet""" # Doc string - *Optional
    def talk(self): # Class method
        print("Hi.  I'm an instance of class Critter.")

# main
crit = Critter() # Creates an instance object (instantiates) from the class Critter named 'crit'
crit.talk() # Every Class object inherits methods defined by the class
            # Class methods are accessed through the dot notation

input("\n\nPress the enter key to exit.")




