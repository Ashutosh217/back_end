from myutils import double_numbers, greet


def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


def test_greet_default():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_custom():
    assert greet("Bob", "Hi") == "Hi, Bob!"
