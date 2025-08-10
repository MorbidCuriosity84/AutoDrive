import pytest
from queue import Queue
from field import Field
from car import Car
from point import Point

@pytest.fixture
def car_A():
    moves = Queue()
    str_moves = ['F', 'F']
    for str_move in str_moves:
        moves.put(str_move)
    return Car('A', Point(0,0), moves, 'E')


@pytest.fixture
def car_B():
    moves = Queue()
    str_moves = ['F', 'F']
    for str_move in str_moves:
        moves.put(str_move)
    return Car('B', Point(3,0), moves, 'W')

@pytest.fixture
def car_C():
    moves = Queue()
    str_moves = ['F', 'F']
    for str_move in str_moves:
        moves.put(str_move)
    return Car('C', Point(2,2), moves, 'S')

@pytest.fixture
def field(car_A, car_B):
    field = Field(3, 3)
    field.cars.append(car_A)
    field.cars.append(car_B)
    return field


def test_is_empty(field):
    assert not field.is_all_moved()

def test_is_empty_2(field):
    for car in field.cars:
        while not car.moves.empty():
            car.moves.get()
    assert field.is_all_moved()