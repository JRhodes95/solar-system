from add import add


def test_add_ints():
    assert add(2, 2) == 4, "Given two ints, it should return the correct answer"


def test_add_floats():
    assert add(
        1.1, 1.2) == 2.3, "Given two floats, it should return the correct answer"


def test_add_int_float():
    assert add(
        1.1, 2) == 3.1, "Given a float and an int, it should return the correct answer"
