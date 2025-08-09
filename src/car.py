from typing import Tuple, List
from queue import Queue


class Car:

    move_map: dict = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)        
    }


    def __init__(self, pos: Tuple[int, int], moves: List[str], direction: str):        
        self.pos: Tuple[int, int] = pos
        self.moves: Queue[str] = moves
        self.direction: str = direction
        self.active = True


    def turn(self, turn: str) -> None:
        match(turn):
            case 'L':
                if self.direction == 'N':
                    self.direction = 'W'
                    return
                if self.direction == 'W':
                    self.direction = 'S'
                    return
                if self.direction == 'S':
                    self.direction = 'E'
                    return
                if self.direction == 'E':
                    self.direction = 'N'
                    return                
            case 'R':
                if self.direction == 'N':
                    self.direction = 'E'
                    return
                if self.direction == 'E':
                    self.direction = 'S'
                    return
                if self.direction == 'S':
                    self.direction = 'W'
                    return
                if self.direction == 'W':
                    self.direction = 'N'
                    return


    def move(self, move: str, size_x: int, size_y: int) -> None:                
                
        if move == 'R' or move =='L':
            self.turn(move)
        else: # Move = 'F'  check valid move then update else ignore move
            if self.check_move(Car.move_map[self.direction], size_x, size_y):
                self.update_pos(Car.move_map[self.direction])


    def check_move(self, move: Tuple[int, int], size_x: int, size_y: int) -> bool:                    
        
        if self.pos[0] + move[0] > size_x:
            return False
        
        if self.pos[0] + move[0] < 0:
            return False

        if self.pos[1] + move[1] > size_y:
            return False
        
        if self.pos[1] + move[1] < 0:
            return False
        
        return True
    
    
    def update_pos(self, move: Tuple[int, int]) -> None:        
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])