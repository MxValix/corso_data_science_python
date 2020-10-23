import itertools
import math


# classe parola chiave, point nome classe
class Point:

    # costruttore, x y parametri per oggetto
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "( " + str(self.x) + ", " + str(self.y) + " )"

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

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

    def __str__(self) -> str:
        return "( " + str(self.day) + ", " + str(self.hour) + " )"

    def delta_hour(self, day_hour) -> int:
        assert (isinstance(day_hour, DayHour))
        return (self.day - day_hour.day) * 24 + (self.hour - day_hour.hour)


class Movement:
    def __init__(self, start: Point, end: Point, start_time: DayHour, end_time: DayHour): #aggiungere tempi
        self.start = start
        self.end = end
        self.start_time = start_time
        self.end_time = end_time

    def length(self) -> float:
        return self.start.distance(self.end)

    def duration(self): #durata
        return self.end_time.delta_hour(self.start_time)

    def speed(self): #velocità media spostamento km/h
        return self.length()

    #def __add__(self, o):
    #   return Path((self.start, self.end, o.start, o.end))

class Path(Movement):
    new_id = itertools.count().__next__

    def __init__(self, points: list, start_t, end_t):
        super().__init__(points[0], points[len(points) - 1], start_t, end_t)
        self.id = Path.new_id()
        #analogo al codice di sopra con la libreria itertools
        #self.id = Path.count
        #Path.count +=1
        self.points = points

    def length(self) -> float:
        return sum([self.points[i].distance(self.points[i + 1]) for i in range(0, len(self.points) - 1)])


if __name__ == '__main__':
    p1 = Point(1, 1)
    print(p1.__str__())

    p2 = Point(0, 0)
    d = p1.distance(p2)
    print(d)

    day1 = DayHour(5, 3)
    print(day1.__str__())
    day2 = DayHour(6, 3)
    diff = day1.delta_hour(day2)
    print(diff)

    try:
        dh = DayHour(3, 57)
    except DayHour.InvalidHour:
        print("errore")

    print(p1 == p2)

    m = Movement(Point(0, 0), Point(1, 1), DayHour(0, 0), DayHour(1, 1))
    path = Path([Point(0, 0), Point(0, 1), Point(1, 1)], DayHour(0, 0), DayHour(1, 1))
    print(path.start)
