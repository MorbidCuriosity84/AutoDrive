from field import Field

class Simulation:

    def __init__(self, field: Field):
        self.field: Field = field


    def run(self):
        for car in self.field.cars:
            if car.moves:
                car.move()