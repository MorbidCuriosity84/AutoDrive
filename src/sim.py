import sys
from typing import Tuple
from field import Field
from point import Point
from car import Car

class Simulation:

    
    DIRECTIONS = ['N', 'S', 'E', 'W']
    COMMANDS = ['F', 'R', 'L']


    def __init__(self, field: Field | None = None):
        self.field: Field = field
        self.steps = 1


    def setup(self) -> None:
        print("Welcome to Auto Driving Car Simulation!")        
        w, h = self.get_width_height()
        self.field = Field(w, h)
        print(f"You have created a field of {w} x {h}")
        self.add_car_or_run()

    def get_width_height(self) -> Tuple[int, int]:
        print("Please enter the width and height of the simulation field in x y format")
        str_w_h = input().strip()
        ls_str_w_H = str_w_h.split(" ")
        
        try:
            assert len(ls_str_w_H) == 2
            w = int(ls_str_w_H[0]) 
            h = int(ls_str_w_H[1]) 
        except ValueError as e:
            print('Values must be integers')
            w, h = self.get_width_height()
        except AssertionError as e:
            print("Must enter two numbers")
            w, h = self.get_width_height()
        
        return w, h


    def add_car_or_run(self) -> None:
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        val = input()

        try:
            val = int(val)
            
            if val == 1:
                self.add_car()
            if val == 2:
                self.run()
            if val != 1 and val != 2:
                raise ValueError()
        except ValueError as e:
            print("Must enter 1 or 2")
            self.add_car_or_run()


    def add_car(self) -> None:                
        name = self.name_car()
        x, y, direction = self.specify_initial_pos(name)
        commands = self.enter_commands(name)
        self.field.cars.append(Car(name, Point(x, y), commands, direction))

        self.add_car_or_run()


    def name_car(self) -> str:
        print("Please enter the name of the car:")
        name = input()

        try:
            assert name
            assert name.isalnum()
        except AssertionError:
            print("Name must be at least one aplhanumeric character")
            self.name_car()

        return name


    def specify_initial_pos(self, name)-> Tuple[int, int, str]:
        print(f"Please enter the initial position of car {name} in x y Direction format")
        pos = input().strip()        
        pos_x_y_dir = pos.split(" ")
        
        try:
            assert len(pos_x_y_dir) == 3
            x = int(pos_x_y_dir[0]) 
            y = int(pos_x_y_dir[1])
            direction = pos_x_y_dir[2] 
            assert x > 0
            assert y > 0
            assert direction.upper() in Simulation.DIRECTIONS
        except ValueError as e:
            print('Values must be integers')
            x, y, direction = self.specify_initial_pos(name)
        except AssertionError as e:
            print("Must enter two positive integers and a direction")
            x, y, direction = self.specify_initial_pos(name)

        return x, y, direction.upper()
        

    def enter_commands(self, name):
        print(f"Please enter the commands for car {name}")
        coms = input()

        try:
            assert all([command.upper() in Simulation.COMMANDS for command in coms])
        except AssertionError:
            print("Commands must be F, R or L")
            coms = self.enter_commands(name)

        return coms.upper()


    def start_over_or_exit(self):
        print("Please choose from the following options:")
        print("[1] Start over")
        print("[2] Exit")

        val = input()
        try:
            val = int(val)
            if val == 1:
                self.steps = 1
                self.setup()
            if val == 2:
                sys.exit(0)
        except ValueError as e:
            print("Must enter 1 or 2")
            self.add_car_or_run()


    def check_collisions(self):
        for car_A in self.field.cars:
            for car_B in self.field.cars:
                if car_A.name == car_B.name:
                    continue
                if car_A.pos == car_B.pos:
                    if car_A.active:
                        print(f"Car {car_A.name} collides with {car_B.name} at {car_A.pos} on step {self.steps}")
                        car_A.active = False
                        car_A.empty_moves()
                    if car_B.active:
                        print(f"Car {car_B.name} collides with {car_A.name} at {car_B.pos} on step {self.steps}")
                        car_B.active = False
                        car_B.empty_moves()


    def run(self):
        print("Your current list of cars are:\n")
        for car in self.field.cars:
            print(car)

        while not self.field.is_all_moved():
            for car in self.field.cars:
                if car.moves and car.active:
                    car.move(car.moves.pop(), self.field.size.x, self.field.size.y)
                    self.check_collisions()
            self.steps += 1

        print("After simulation, the result is:\n")
        for car in self.field.cars:
            print(car)
        
        self.start_over_or_exit()

