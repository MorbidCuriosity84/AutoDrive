from field import Field

class Simulation:

    def __init__(self, field: Field):
        self.field: Field = field
        self.steps = 1


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
        while not self.field.is_all_moved():
            for car in self.field.cars:
                if not car.moves.empty() and car.active:
                    car.move(car.moves.get(), self.field.size.x, self.field.size.y)
                    self.check_collisions()
            self.steps += 1
            