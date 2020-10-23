import math


# classe parola chiave, point nome classe
class Point:

    # costruttore, x y parametri per oggetto
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, point) -> float:
        assert (isinstance(point, Point))
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


if __name__ == '__main__':
    p1 = Point(1, 1)
    p2 = Point(0, 0)
    d = p1.distance(p2)
    print(d)