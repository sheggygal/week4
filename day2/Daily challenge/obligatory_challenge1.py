import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

# Example usage:
c1 = Circle(radius=3)
c2 = Circle(diameter=4)
print("Circle 1:", c1)
print("Circle 2:", c2)
print("Area of Circle 1:", c1.area)
print("Diameter of Circle 2:", c2.diameter)

c3 = c1 + c2
print("Circle 3 (Circle 1 + Circle 2):", c3)

print("Is Circle 1 bigger than Circle 2?", c1 > c2)
print("Are Circle 1 and Circle 2 equal?", c1 == c2)

circle_list = [c1, c2, c3]
sorted_circle_list = sorted(circle_list)
print("Sorted Circles:", sorted_circle_list)
