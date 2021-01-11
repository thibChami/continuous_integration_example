from fibonacci import fibonacci
import pytest


@pytest.mark.parametrize('n', [0, 1, 5, -1])
def test_fibonacci(n):
    f = fibonacci(n)
    assert(type(f) == int and f >= 0), \
        'Fibonacci sequence should return a positive integer'
