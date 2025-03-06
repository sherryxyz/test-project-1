from example import get_weather, add, divide
import pytest

# def test_get_weather():
#     assert get_weather(21) == "cold"

def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(-1, 1) == 0, "-1 + 1 should be 0"
    assert add(0, 0) == 0, "0+0 should be 0"

def test_divde():
    with pytest.raises(ValueError, match = "Cannot divide by zero"):
        divide(10, 0)


# @pytest.fixture # to crete a fresh instance before each test
# def user_manager():
#     return UserManager()


@pytest.mark.parametrize("num, num2, expected", [
      (2, 3, 5),
      (-1, 1, 0),
      (0, 0, 0),
])

def test_add(num, num2, expected):
    assert add(num, num2) == expected