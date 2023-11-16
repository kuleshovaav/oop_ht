from math import sqrt
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({round(self.x, 3)}; {round(self.y, 3)})"
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    def distance(self, other):
        if other.__class__ != self.__class__:
            raise IOError("\nНедопустимый аргумент вычисления расстояния")
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

