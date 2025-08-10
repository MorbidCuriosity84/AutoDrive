import pytest
from queue import Queue
from field import Field
from car import Car
from point import Point

@pytest.fixture
def car_A():
    return Car('A', Point(0,0), "FF", 'E')


@pytest.fixture
def car_B():
    return Car('B', Point(3,0), "FF", 'W')

@pytest.fixture
def car_C():
    return Car('C', Point(2,2), "FF", 'S')

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
        while car.moves:
            car.moves.pop()
    assert field.is_all_moved()