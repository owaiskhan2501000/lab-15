from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Child Classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

print("Circle Area:", circle.area())        # Output: Circle Area: 78.5
print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24
print("Triangle Area:", triangle.area())    # Output: Triangle Area: 6.0
