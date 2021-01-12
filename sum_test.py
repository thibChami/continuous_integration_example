from sum import mysum
import pytest


@pytest.mark.parametrize('numbers, output', [
    ([], 0),
    ([10, 20, 30], 60),
    ([0.1, 1.2, 2.3, 3.4, 4.5], 11.5),
    ([1,2,3,4], 10)])
def test_mysum(numbers, output):
    assert mysum(numbers) == output
    assert (len(numbers)%2) == 1
