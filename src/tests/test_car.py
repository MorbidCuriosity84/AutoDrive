import pytest 
from queue import Queue
from car import Car
from field import Field

@pytest.fixture
def car() -> Car:
    list_moves = ['F', 'R', 'F', 'R', 'F', 'F', 'R', 'F', 'F']
    move_queue = Queue()
    for move in list_moves:
        move_queue.put(move)
    car = Car((0,0), move_queue, 'S')
    return car
    

@pytest.fixture
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

def test_move(car, field):
    move = car.moves.get()
    assert move == 'F'
    assert car.direction == 'S'
    car.move(move, field.size[0], field.size[1])
    assert car.pos == (0,0)

def test_move_2(car, field):
    move = car.moves.get()
    move = car.moves.get()
    assert move == 'R'
    assert car.direction == 'S'
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'W'

def test_move_2(car, field):
    move = car.moves.get()
    move = car.moves.get()
    assert move == 'R'
    assert car.direction == 'S'
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'W'

def test_move_3(car, field):
    for _ in range(2):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'F'
    assert car.direction == 'W'
    assert car.pos == (0, 0)
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'W'
    assert car.pos == (0, 0)

def test_move_4(car, field):
    for _ in range(3):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'R'
    assert car.direction == 'W'
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'N'

def test_move_5(car, field):
    for _ in range(4):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'F'
    assert car.direction == 'N'
    assert car.pos == (0,0)
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'N'
    assert car.pos == (0,1)

def test_move_6(car, field):
    for _ in range(5):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'F'
    assert car.direction == 'N'
    assert car.pos == (0,1)
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'N'
    assert car.pos == (0,1)

def test_move_7(car, field):
    for _ in range(6):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'R'
    assert car.direction == 'N'
    assert car.pos == (0,1)
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'E'
    assert car.pos == (0,1)

def test_move_8(car, field):
    for _ in range(7):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'F'
    assert car.direction == 'E'
    assert car.pos == (0,1)
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'E'
    assert car.pos == (1,1)

def test_move_9(car, field):
    for _ in range(8):
        move = car.moves.get()
        car.move(move, field.size[0], field.size[1])    
    move = car.moves.get()
    assert move == 'F'
    assert car.direction == 'E'
    assert car.pos == (1,1)
    car.move(move, field.size[0], field.size[1])
    assert car.direction == 'E'
    assert car.pos == (1,1)