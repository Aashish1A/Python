# Define a circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle():
    def __init__(self,radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.13 * self.radius ** 2
    
    def calc_perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(21)
print("The area of circle is : ",c1.calc_area())
print("The perimeter of circle is : ",c1.calc_perimeter())