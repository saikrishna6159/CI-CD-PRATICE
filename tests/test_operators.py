from src.mathsoperators import add,subtract
def test_add():
    assert add(2,3) ==5
    assert add(5,6) ==11
    assert add(3,3) ==6
def test_subtract():
    assert subtract(2,3) ==-1
    assert subtract(3,3) ==0
    assert subtract(6,5) ==1