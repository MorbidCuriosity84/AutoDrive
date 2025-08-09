from dataclasses import dataclass
from typing import Any

@dataclass
class Point:

    x: int
    y: int

    def __add__(self, other: Any):
        if not isinstance(other, Point):
            raise ValueError(f"Invalid value. Can only add two Points, not {type(self)} and {type(other)}")
        return Point(self.x + other.x, self.y + other.y)        

    def __radd__(self, other: Any):
        if not isinstance(other, Point):
            raise ValueError(f"Invalid value. Can only add two Points, not {type(other)} and {type(other)}")
        return Point(self.x + other.x, self.y + other.y)
    