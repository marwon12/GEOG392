#Marwon Haridi
#Lab 3'

#Importing libraries
import math

#example of classes
'''
class fruit:
    def __init__(self,color,age,rotten):
        self.color = color
        self.age = age
        self.rotten = rotten
    def get_color(self):
        return self.color
    def get_age(self):
        retun self.age
class apple(fruit):
    def get_age(self):
        return self.age**0.25
class banana(fruit):
    def get_age(self):
        retun self.age**2
'''

#classes
class Shape:
    def __init__init(self):
        pass
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
        
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return (self.b * self.h)/2
        
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return r * r * math.pi
    

#writing file example
'''
o_handle = open(r"directory", "w")
o_handle.write("This is how you write to a file\n")
o_handle.close()
'''

#File IO
file = open("shapes.txt", "r")
myread = file.readlines()
for line in myread:
    
file.close()



