import pytest
from unittest.mock import patch, call
from queue import Queue
from sim import Simulation
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
def car_D():
    moves = Queue()
    str_moves = ['F', 'F']
    for str_move in str_moves:
        moves.put(str_move)
    return Car('B', Point(3,1), moves, 'W')

@pytest.fixture
def field(car_A, car_B, car_C):
    field = Field(3, 3)
    field.cars.append(car_A)
    field.cars.append(car_B)
    field.cars.append(car_C)
    return field

@pytest.fixture
def field_2(car_A, car_D):
    field = Field(3, 3)
    field.cars.append(car_A)
    field.cars.append(car_D)
    return field

@pytest.fixture
def sim(field):
    return Simulation(field)

@pytest.fixture
def sim_2(field_2):
    return Simulation(field_2)

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock:
        yield mock


def test_sim_collisions(sim):
    assert all([car.active for car in sim.field.cars])

def test_sim_collisions_2(sim):
    sim.run()
    assert all([not car.active for car in sim.field.cars])

def test_sim_collisions_3(sim, mock_print):
    sim.run()
    mock_print.assert_called()
    assert mock_print.call_count == 3    
    call_A = call('Car A collides with B at Point(x=2, y=0) on step 2')
    call_B = call('Car B collides with A at Point(x=2, y=0) on step 2')
    call_C = call('Car C collides with A at Point(x=2, y=0) on step 2')
    calls = [call_A, call_B, call_C]    
    mock_print.assert_has_calls(calls)

def test_sim_collisions_4(sim_2, mock_print):
    sim_2.run()
    mock_print.assert_not_called()
    

