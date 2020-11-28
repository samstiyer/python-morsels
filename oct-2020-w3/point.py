"""
The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

Example usage:

>>> p1 = Point(1, 2, 3)
>>> p1
Point(x=1, y=2, z=3)
>>> p2 = Point(1, 2, 3)
>>> p1 == p2
True
>>> p2.x = 4
>>> p1 == p2
False
>>> p2
Point(x=4, y=2, z=3)

If you finish the base exercise quickly, consider working through a bonus or two.

Bonus 1

For the first bonus, I'd like you to allow Point objects to be added and subtracted from each other. ✔️

>>> p1 = Point(1, 2, 3)
>>> p2 = Point(4, 5, 6)
>>> p1 + p2
Point(x=5, y=7, z=9)
>>> p3 = p2 - p1
>>> p3
Point(x=3, y=3, z=3)

Bonus 2

For the second bonus, I'd like you to allow Point objects to be scaled up and down by numbers. ✔️

>>> p1 = Point(1, 2, 3)
>>> p2 = p1 * 2
>>> p2
Point(x=2, y=4, z=6)

Bonus 3

For the third bonus, I'd like you to allow Point objects to be unpacked using multiple assignment like this ✔️:

>>> p1 = Point(1, 2, 3)
>>> x, y, z = p1
>>> (x, y, z)
(1, 2, 3)

"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, o: object) -> bool:
        return self.__class__ == o.__class__ and vars(self) == vars(o)

    def __add__(self, op):
        return Point(self.x + op.x, self.y + op.y, self.z + op.z)

    def __sub__(self, op):
        return Point(self.x - op.x, self.y - op.y, self.z - op.z)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n, self.z * n)

    def __rmul__(self, n):
        return Point(self.x * n, self.y * n, self.z * n)

    def __iter__(self):
        for attr in vars(self).values():
            yield attr
