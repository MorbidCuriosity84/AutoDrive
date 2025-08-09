from dataclasses import dataclass
from typing import Any

@dataclass
class Point:

    x: int
    y: int

    def __add__(self, other: Any):
        assert isinstance(other, Point)
        return Point(self.x + other.x, self.y + other.y)        

    def __radd__(self, other: Any):
        assert isinstance(other, Point)
        return Point(self.x + other.x, self.y + other.y)
    