from typing import List
from point import Point


class Car:

    move_map: dict[str, Point] = {
        'N': Point(0, 1),
        'S': Point(0, -1),
        'E': Point(1, 0),
        'W': Point(-1, 0)        
    }


    def __init__(self, name: str, pos: Point, moves: str, direction: str):        
        self.name = name
        self.pos: Point = pos
        self.moves: List[str] = list(moves[::-1])
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


    def check_move(self, move: Point, size_x: int, size_y: int) -> bool:
        pos_after_move = self.pos + move

        if pos_after_move.x > size_x:
            return False
        
        if pos_after_move.x < 0:
            return False

        if pos_after_move.y > size_y:
            return False
        
        if pos_after_move.y < 0:
            return False
        
        return True
    
    
    def update_pos(self, move: Point) -> None:        
        self.pos += move

    def empty_moves(self):
        self.moves = []

    def __repr__(self):        
        moves = f', {"".join([mv for mv in self.moves[::-1]])}' if self.moves else ''
        return f"- {self.name}, ({self.pos.x},{self.pos.y}) {self.direction}{moves}"
