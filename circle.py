class Circle:
    def __init__(self, radius=10):
        self.radius = radius
        self.pi = 22 / 7
    
    def calculate_area(self):
        return self.pi * (self.radius ** 2)

# Create an instance of Circle
circle = Circle()

# Calculate and print the area
print("Area of the circle:", circle.calculate_area())