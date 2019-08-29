from solutions.SUM import sum_solution
from hypothesis import given
from hypothesis.strategies import integers


@given(
    x=integers(min_value=0, max_value=100),
    y=integers(min_value=0, max_value=100)
)
def test_sum(x, y):
    assert sum_solution.compute(x, y) == x + y
