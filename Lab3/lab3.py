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
    def getArea(self):
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
        return r
    

#writing file example
'''
o_handle = open(r"directory", "w")
o_handle.write("This is how you write to a file\n")
o_handle.close()
'''

#File IO
file = open("shapes.txt", "r")
myread = file.readlines()
file.close()

for line in myread:
    #print(line)
    data_items = line.split(",")
    #print (data_items[0])
    if data_items[0] == "Rectangle":
        r = Rectangle(float(data_items[1]),float(data_items[2]))
        print(r.getArea())
    elif data_items[0] == "Triangle":
        t= Triangle(float(data_items[1]),float(data_items[2]))
        print(t.getArea())
    else:
        c = Circle(float(data_items[1]))
        print(c)
    
'''
i_handle = open("shapes.txt", "r")
i_handle.seek(0)
data_text = i_handle.read().strip.split("\n")
print(data_txt)
i_handle.close()
'''



