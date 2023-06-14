import pytest

from app_window import plus

def test_plus_zero ():
    assert plus(0,0) == 0

def test_plus ():
    assert plus(2,3) == 5
    assert plus(3,3) == 6
    assert plus(4,3) == 7
    assert plus(5,3) == 8

def test_plus_negative():
    assert plus(2, -1) == 1

    if __name__ == '__main__':
        pytest.main()