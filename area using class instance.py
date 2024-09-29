import math
class rectangle:
    def r_area (self):
        self.width= int(input("enter the width of rectangle:"))
        self.length=int(input("enter the length of rectange:"))
        return (self.width*self.length)

class traingle:
    def t_area (self):
        self.height=int(input("enter the height of traingle:"))
        self.base=int(input("enter the base of traingle:"))
        return (0.5*self.height*self.base)

class circle (rectangle, traingle):
    def c_area (self):
        self.radius=int(input("enter the radius of circle:"))
        return(math.pi*self.radius**2)

c=circle()
print ("Area of rectangle ",c.r_area())
print("Area of traingle ",c.t_area ())
print("Area of circle ",c.c_area())
