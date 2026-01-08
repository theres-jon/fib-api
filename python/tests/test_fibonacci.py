from app.fibonacci import fibonacci


def test_fibonacci_zero():
    assert fibonacci(0) == []


def test_fibonacci_one():
    assert fibonacci(1) == [0]


def test_fibonacci_two():
    assert fibonacci(2) == [0, 1]


def test_fibonacci_sequence():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_negative():
    assert fibonacci(-5) == []
