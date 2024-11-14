import math

class Figure:
     unit = 'cm '

     def __init__(self):
          self.__perimeter = 0

     @property
     def perimeter(self):
          return self.__perimeter

     @perimeter.setter
     def perimeter(self, value):
          self.__perimeter = value

     def calculate_area(self):
          raise NotImplementedError("Subclasses must implement this method")


     def calculate_area(self):
          raise NotImplementedError("Subclasses must implement this method")

     def info(self):
          raise NotImplementedError("Subclasses must implement this method")


class Square(Figure):
     def __init__(self, side_length):
          super().__init__()
          self.__side_length = side_length
          self.calculate_perimeter()

     def calculate_area(self):
          return self.__side_length ** 2

     def calculate_perimeter(self):
          self.perimeter = 4 * self.__side_length

     def info(self):
          return f"Square side length: {self.__side_length}{self.unit}, perimeter: {self.perimeter}{self.unit}, area: {self.calculate_area()}{self.unit}^2"


class Rectangle(Figure):
     def __init__(self,  length,  width):
          super().__init__()
          self.__length = length
          self.__width = width
          self.calculate_perimeter()

     def calculate_area(self):
          return self.__length * self.__width

     def calculate_perimeter(self):
          self.perimeter = 2 * (self.__length + self.__width)

     def info(self):
          return f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {self.calculate_area()}{self.unit}^2."
     
squares = [Square(5), Square(25)]
rectangles = [Rectangle(3, 7), Rectangle(4, 9), Rectangle(6, 10)]

for square in squares:
     print(square.info())

for rectangle in rectangles:
     print(rectangle.info())