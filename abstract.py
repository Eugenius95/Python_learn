#import module and import
from abc import ABC, abstractmethod

class shape():
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class square(shape):
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return 4 * self.__side
        
        
#shape_obj = shape()
square_obj = square(10)
print(square_obj.area())
                