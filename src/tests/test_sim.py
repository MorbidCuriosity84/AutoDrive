import pytest
from unittest.mock import patch, call, Mock
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
    return Car('A', Point(0,0), "FF", 'E')


@pytest.fixture
def car_B():
    return Car('B', Point(3,0), "FF", 'W')

@pytest.fixture
def car_C():
    return Car('C', Point(2,2), "FF", 'S')

@pytest.fixture
def car_D():
    moves = Queue()
    str_moves = ['F', 'F']
    for str_move in str_moves:
        moves.put(str_move)
    return Car('B', Point(3,1), "FF", 'W')

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

@pytest.fixture
def mock_input():
    with patch('builtins.input') as mock:
        yield mock

def test_sim_collisions(sim):
    assert all([car.active for car in sim.field.cars])

@patch.object(Simulation, 'setup')
@patch.object(Simulation, 'start_over_or_exit')
def test_sim_collisions_2(start_or_exit, setup, sim):
    start_or_exit.return_value = None
    setup.return_value = None
    sim.run()
    assert all([not car.active for car in sim.field.cars])

@patch.object(Simulation, 'setup')
@patch.object(Simulation, 'start_over_or_exit')
def test_sim_collisions_3(start_over_or_exit, setup, sim, mock_print):
    start_over_or_exit.return_value = None
    setup.return_value = None
    sim.run()
    mock_print.assert_called()
    assert mock_print.call_count == 11    
    call_A = call('Car A collides with B at Point(x=2, y=0) on step 2')
    call_B = call('Car B collides with A at Point(x=2, y=0) on step 2')
    call_C = call('Car C collides with A at Point(x=2, y=0) on step 2')
    calls = [call_A, call_B, call_C]    
    mock_print.assert_has_calls(calls)

@patch.object(Simulation, 'setup')
@patch.object(Simulation, 'start_over_or_exit')
def test_sim_collisions_4(setup, start_or_exit, sim_2, mock_print):
    start_or_exit.return_value = None
    setup.return_value = None
    sim_2.run()
    mock_print.assert_called()
    

@patch.object(Simulation, 'add_car_or_run')
@patch.object(Simulation, 'get_width_height')
@patch('builtins.print')
@patch('builtins.input')
def test_sim_setup(mock_input, mock_print, mock_get_width_height, mock_add_car_or_run, sim_2):
    mock_get_width_height.return_value = (10, 10)
    mock_add_car_or_run.return_value = None
    mock_input.return_value = "10 10"
    sim_2.setup()
    mock_print.assert_called()
    assert mock_print.call_count == 2
    mock_get_width_height.assert_called_once()
    mock_add_car_or_run.assert_called_once()
    mock_print.assert_has_calls([call("Welcome to Auto Driving Car Simulation!"), call("You have created a field of 10 x 10")])

@patch.object(Simulation, 'add_car')
@patch.object(Simulation, 'run')
@patch('builtins.input')
def test_sim_add_car_or_run(mock_input, mock_run, mock_add_car, sim_2):
    mock_input.return_value = "1"
    sim_2.add_car_or_run()
    mock_add_car.assert_called()
    mock_run.assert_not_called()
    

@patch.object(Simulation, 'add_car')
@patch.object(Simulation, 'run')
@patch('builtins.input')
def test_sim_add_car_or_run_2(mock_input, mock_run, mock_add_car, sim_2):
    mock_input.return_value = "2"
    sim_2.add_car_or_run()
    mock_add_car.assert_not_called()
    mock_run.assert_called()


@patch.object(Simulation, 'add_car')
@patch('builtins.input')
def test_sim_add_car_or_run_3(mock_input, mock_add_car, sim_2):
    mock_input.side_effect = ['A', '1']
    sim_2.add_car_or_run()
    mock_input.call_count == 2
    mock_add_car.assert_called_once()
    

@patch.object(Simulation, 'run')
@patch('builtins.input')
def test_sim_add_car_or_run_4(mock_input, mock_run, sim_2):
    mock_input.side_effect = ['A', '2']
    sim_2.add_car_or_run()
    mock_input.call_count == 2
    mock_run.assert_called_once()


@patch.object(Simulation, 'name_car')
@patch.object(Simulation, 'specify_initial_pos')
@patch.object(Simulation, 'enter_commands')
@patch.object(Simulation, 'add_car_or_run')
def test_sim_add_car(mock_add_car_or_run, mock_enter_commands, mock_spec_init_pos, mock_name, sim):
    mock_name.return_value = 'A'
    mock_spec_init_pos.return_value = (1, 2, 'N')
    mock_enter_commands.return_value = "FFRRFFFFL"
    sim.field.cars = []
    sim.add_car()
    car = sim.field.cars[0]
    assert car.name == 'A'
    assert car.pos == Point(1, 2)
    assert car.moves == [char for char in "LFFFFRRFF"]
    assert car.direction == 'N'
    mock_add_car_or_run.assert_called()


@patch('builtins.input')
@patch('builtins.print')
def test_name_car(mock_print, mock_input, sim):
    mock_input.side_effect = ['_', 'A']
    sim.name_car()
    mock_print.assert_has_calls([call('Please enter the name of the car:'), call('Name must be at least one aplhanumeric character')])    


@patch('builtins.input')
@patch('builtins.print')
def test_name_car_2(mock_print, mock_input, sim):
    mock_input.side_effect = ['A']
    name = sim.name_car()
    assert name == 'A'


@patch('builtins.input')
def test_specify_pos(mock_input, sim):
    mock_input.side_effect = ["10 15 N"]
    x, y, dir = sim.specify_initial_pos('A')
    assert x == 10
    assert y == 15
    assert dir == 'N'


@patch('builtins.input')
@patch('builtins.print')
def test_specify_pos_2(mock_print, mock_input, sim):
    mock_input.side_effect = ["10 N", "10 15 N"]
    sim.specify_initial_pos('A')
    mock_print.assert_has_calls([call("Please enter the initial position of car A in x y Direction format"), call("Must enter two positive integers and a direction")])


@patch('builtins.input')
@patch('builtins.print')
def test_specify_pos_3(mock_print, mock_input, sim):
    mock_input.side_effect = ["10 15 a", "10 15 N"]
    sim.specify_initial_pos('A')
    mock_print.assert_has_calls([call("Please enter the initial position of car A in x y Direction format"), call("Must enter two positive integers and a direction")])


@patch('builtins.input')
@patch('builtins.print')
def test_specify_pos_4(mock_print, mock_input, sim):
    mock_input.side_effect = ["a b c", "10 15 N"]
    sim.specify_initial_pos('A')
    mock_print.assert_has_calls([call("Please enter the initial position of car A in x y Direction format"), call("Values must be integers")])


@patch('builtins.input')
@patch('builtins.print')
def test_specify_pos_5(mock_print, mock_input, sim):
    mock_input.side_effect = ["-1 -1 c", "10 15 N"]
    sim.specify_initial_pos('A')
    mock_print.assert_has_calls([call("Please enter the initial position of car A in x y Direction format"), call("Must enter two positive integers and a direction")])


@patch('builtins.input')
@patch('builtins.print')
def test_enter_commands(mock_print, mock_input, sim):
    mock_input.side_effect = ["FFFRRFFLLF"]
    coms = sim.enter_commands('A')
    mock_print.assert_has_calls([call("Please enter the commands for car A")])
    assert coms == "FFFRRFFLLF"


@patch('builtins.input')
@patch('builtins.print')
def test_enter_commands_2(mock_print, mock_input, sim):
    mock_input.side_effect = ["flrf"]
    coms = sim.enter_commands('A')
    mock_print.assert_has_calls([call("Please enter the commands for car A")])
    assert coms == "FLRF"


@patch('builtins.input')
@patch('builtins.print')
def test_enter_commands_3(mock_print, mock_input, sim):
    mock_input.side_effect = ["ABCDEFG", "FFFRRFFLLF"]
    sim.enter_commands('A')
    mock_print.assert_has_calls([call("Please enter the commands for car A"), call("Commands must be F, R or L")])