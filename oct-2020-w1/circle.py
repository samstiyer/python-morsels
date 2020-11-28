import math


class Circle:
    def __init__(self, radius: int = 1):

        if radius < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self._radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self._radius = new_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @area.setter
    def area(self, new_area):
        raise AttributeError
