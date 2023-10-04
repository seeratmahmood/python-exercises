# 1- create a Point class

from abc import ABC, abstractmethod


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 2 - creating a Shape class - making it abstract

class shape(ABC):
    def __init__(self, name, colour, x, y):
        self.name = name
        self.colour = colour
        self.position = point(x, y)

    # creating abstract methods

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getCenterPoint(self):
        pass

#3 - creating a Rectangle class

class rectangle(shape):
    def __init__(self, name, colour, x, y, width, height):
        super().__init__(name, colour, x, y)
        self.width = width
        self.height = height

    # implemented isSquare method
    def isSquare(self):
        if self.height == self.width:
            return True
        else:
            return False

# overriding and implementing abstract methods

    def getArea(self):
        return self.width * self.height

    def getCenterPoint(self):
        return self.position.x, self.position.y

# creating objects

r1 = rectangle("rectangle 1", "blue", 1, 1, 4, 7)
r2 = rectangle("rectangle 2", "green", 2, 2, 5, 5)
r3 = rectangle("rectangle 3", "pink", 3, 3, 3, 6)

rectangles = [r1, r2, r3]

for r in rectangles:
    print(f"Name: {r.name}")
    print(f"Colour: {r.colour}")
    print(f"Position: {r.position.x}, {r.position.y}")
    print(f"Width: {r.width}")
    print(f"Height: {r.height}")
    print(f"Is Square: {r.isSquare()}")
    print(f"Area: {r.getArea()}")
    print(f"Center Point: {r.getCenterPoint()}\n")

if __name__ == "shape":
    shape()

#4 - Creating circle class

import math

class circle(shape):
    def __init__(self, name, colour, x, y, radius):
        super().__init__(name, colour, x, y)
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getCenterPoint(self):
        return self.position.x, self.position.y

# creating objects

c1 = circle(f"circle 1", "red", 1, 1, 5)
c2 = circle(f"circle 2", "yellow", 2, 2, 10)
c3 = circle(f"circle 3", "blue", 3, 3, 12)

circles = [c1, c2, c3]

for c in circles:
    print(f"Name: {c.name}")
    print(f"Colour: {c.colour}")
    print(f"Position: {c.position.x}, {c.position.y}")
    print(f"Radius: {c.radius}")
    print(f"Area: {c.getArea()}")
    print(f"Center Point: {c.getCenterPoint()}\n")

if __name__ == "shape":
    shape()
