from typing import List
from car import Car
from point import Point


class Field:
    
    def __init__(self, size_x: int, size_y: int):
        
        self.size: Point = Point(size_x, size_y)
        self.cars: List[Car] = []


    def is_all_moved(self):
        return all([not car.moves for car in self.cars])
    