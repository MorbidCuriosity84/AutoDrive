import pytest
from point import Point

@pytest.fixture
def point_A():
    return Point(0, 0)

@pytest.fixture
def point_B():
    return Point(1, 1)

@pytest.fixture
def point_C():
    return Point(-1, -1)

def test_add_point(point_A, point_B):
    assert point_A + point_B == Point(1, 1)

def test_add_point_2(point_A, point_B):
    assert point_B + point_A == Point(1, 1)

def test_add_point_3(point_C, point_B):
    assert point_C + point_B == Point(0, 0)

def test_add_point_4(point_B, point_C):
    assert point_B + point_C == Point(0, 0)

def test_add_point_5(point_C, point_A):
    assert point_C + point_A == Point(-1, -1)

def test_add_point_6(point_A, point_C):
    assert point_A + point_C == Point(-1, -1)

def test_add_bad_value(point_A):
    with pytest.raises(ValueError):
        point_A + 1

def test_add_bad_value_2(point_A):
    with pytest.raises(ValueError):
        point_A + 'a'

def test_add_bad_value_3(point_A):
    with pytest.raises(ValueError):
        point_A + 1.01

def test_add_bad_value_4(point_A):
    with pytest.raises(ValueError):
        point_A + {'a': 1}

def test_add_bad_value_5(point_A):
    with pytest.raises(ValueError):
        point_A + ['a']