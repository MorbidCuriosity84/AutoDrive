from typing import Tuple, List

class Car:

    move_map: dict = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)        
    }

    def __init__(self, pos: Tuple[int, int], moves: List[str], direction: str):        
        self.pos: Tuple[int, int] = pos
        self.moves: List[str] = moves
        self.direction: str = direction
        self.active = True

    def move(self, size_x: int, size_y: int):
        pass

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
    
    def update_pos(self, move: Tuple[int, int]):        
        self.pos = (self.pos + move[0], self.pos[1] + move[1])