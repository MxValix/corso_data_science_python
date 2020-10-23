import math


# classe parola chiave, point nome classe
class Point:

    # costruttore, x y parametri per oggetto
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, point) -> float:
        assert (isinstance(point, Point)) # controllare che il tipo sia giusto
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class DayHour:

    class InvalidHour(Exception):

        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    def __init__(self, day: int, hour: int):
        if hour > 24 or hour < 0:
            raise DayHour.InvalidHour()
        self.day = day
        self.hour = hour

    def delta_hour(self, day_hour) -> int:
        assert (isinstance(day_hour, DayHour))
        return (self.day - day_hour.day) * 24 + (self.hour - day_hour.hour)


if __name__ == '__main__':
    p1 = Point(1, 1)
    p2 = Point(0, 0)
    d = p1.distance(p2)
    print(d)
    
    day1 = DayHour(5, 3)
    day2 = DayHour(6, 3)
    diff = day1.delta_hour(day2)
    print(diff)
    
    try:
        dh = DayHour(3, 57)
    except DayHour.InvalidHour:
        print("errore")


