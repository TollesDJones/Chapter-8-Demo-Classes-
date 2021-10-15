"""
Create a class, Triangle.
 Its __init__() method should take
 angle1, angle2, and angle3 as arguments.
 Make sure to set these appropriately in the body of the __init__()method
 don't forget about the'self' argument

Create a variable named number_of_sides and set it equal to 3.

Create a method named check_angles.
 Sum the triangle's three angles.It should return True if the sum of
 self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.

Create an instance of your triangle class named my_triangle. Pass it three angles
 that sum to 180 (e.g. 90, 30, 60).

Print out my_triangle.number_of_sides and print out my_triangle.check_angles().
"""





















class Triangle:
    numSides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def checkAngles(self):
       sum_of_Angels = self.angle1 + self.angle2 + self.angle3

       if sum_of_Angels == 180:
           return True
       else:
           return False


T1 = Triangle(90, 30, 60)
T2 = Triangle(60, 60, 60)
print(T1.numSides)
print(T1.checkAngles())
print(T2.checkAngles())