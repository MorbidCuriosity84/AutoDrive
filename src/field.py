from typing import Tuple, List
from car import Car

class Field:
    
    def __init__(self, size_x: int, size_y: int):
        
        self.size: Tuple[int, int] = (size_x, size_y)
        self.cars: List[Car] = []


    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    