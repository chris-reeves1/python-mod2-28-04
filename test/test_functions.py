import pytest
from pytest_files.my_functions import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    assert add(200, 300) == 500

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# fixture
#@pytest.fixture
#def x():
 #   return Area(10, 5)

#def test_area(x):
#    assert x.area() == 50

@pytest.mark.parametrize("length, width, area", [(5, 10, 50),(10,10,100),(5,5,25)])
def test_multiple_cases(length, width, area):
    x = Area(length, width)
    assert x.area() == area

@pytest.mark.skip(reason="something...")
def test_skip():
    assert add(1, 2) == 3 