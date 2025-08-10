from queue import Queue
from sim import Simulation
from field import Field
from car import Car
from point import Point

if __name__ == '__main__':

    moves = Queue()
    str_moves = ['F', 'F']
    for str_move in str_moves:
        moves.put(str_move)
    car_A =  Car('A', Point(0,0), moves, 'E')
    
    moves = Queue()
    for str_move in str_moves:
        moves.put(str_move)
    car_B = Car('B', Point(3,0), moves, 'W')

    moves = Queue()
    for str_move in str_moves:
        moves.put(str_move)
    car_C = Car('C', Point(2,2), moves, 'S')

    field = Field(3, 3)
    field.cars.append(car_A)
    field.cars.append(car_B)
    field.cars.append(car_C)
    sim = Simulation(field)
    sim.run()
    