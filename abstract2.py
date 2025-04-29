from abc import ABC, abstractmethod
import math

# 1. Abstract class 'Shape'
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

# 2a. Concrete class 'Rectangle'
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# 2b. Concrete class 'Circle'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# 3. Outside the classes
rectangle = Rectangle(width=5, height=10)
circle = Circle(radius=7)

print("Rectangle area:", rectangle.calculate_area())
print("Circle area:", circle.calculate_area())
