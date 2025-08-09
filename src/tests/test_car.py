import pytest 
from car import Car
from field import Field

@pytest.fixture(scope='session')
def car() -> Car:
    car = Car((0,0), ['F', 'R', 'F', 'R', 'F', 'F', 'R', 'F', 'F'], 'S')
    return car
    

@pytest.fixture(scope='session')
def field() -> Field:
    field = Field(1, 1)
    return field

def test_check_move(car, field):        
    valid = car.check_move(Car.move_map[car.direction], field.size[0], field.size[1])
    assert not valid

def test_check_move_2(car, field):
    car.direction = 'W'
    valid = car.check_move(Car.move_map[car.direction], field.size[0], field.size[1])
    assert not valid

def test_check_move_3(car, field):
    car.direction = 'N'
    valid = car.check_move(Car.move_map[car.direction], field.size[0], field.size[1])
    assert valid

def test_check_move_4(car, field):
    car.direction = 'E'
    valid = car.check_move(Car.move_map[car.direction], field.size[0], field.size[1])
    assert valid