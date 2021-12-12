# Q1
from abc import ABC, abstractmethod
from turtle import *
speed(0)

# abstract class, and super class too
class TwoDShape(ABC):
    @abstractmethod
    def draw(self): # polymorphism draw definetion 1
        pass

# down here are all concrete classes, and sub class too
class Line(TwoDShape):
    def __init__(self, length):
        self.l = length

    def draw(self): # def2
        fd(self.l)

class Rectangle(TwoDShape):
    def __init__(self, width, height):
        self.w = width
        self.h = height
    
    def draw(self): #def3
        for i in range(2):
            fd(self.w)
            lt(90)
            fd(self.h)
            lt(90)

class Circle(TwoDShape):
    def __init__(self, radius):
        self.r = radius

    def draw(self): # def4
        circle(self.r)

# Q2
class Square(TwoDShape):
    def __init__(self, size):
        self.s = size

    def draw(self): # def5
        for i in range(4):
            fd(self.s)
            lt(90)

drawings = [Circle(60), Line(100), Rectangle(50, 75), Line(200), Circle(100), Square(50)]

for draw in drawings:
    draw.draw()

done()



# Q3
from abc import ABC, abstractmethod

# abstract class and at the same time this is a super class(parent class) too
class Transportation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.st = start_place
        self.ed = end_place
        self.d = distance

    @abstractmethod
    def find_cost(self): # polymorphism, find_cost definetion 1
        pass

# down here are all concrete classes, and they are sub class (childe class) at the same time
class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance) # inheritance from the super class(parent class)

    def find_cost(self): # def2
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance) # inheritance

    def find_cost(self): # def2
        return 40 * self.d

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance) # inheritance
        self.sta = station

    def find_cost(self): # def3
        return 5 * self.sta

print(Walk("KMITL", "KMITL SCB Bank", 0.6).find_cost())
print(Taxi("KMITL SCB Bank", "Ladkrabang Station", 5).find_cost())
print(Train("Ladkrabang Station", "Payathai Station", 40, 6).find_cost())
print(Taxi("Payathai Station", "The British Council", 3).find_cost())
