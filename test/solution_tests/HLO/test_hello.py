from solutions.HLO import hello_solution


def test_hello():
    assert hello_solution.hello("Hello") == hello_solution.ALWAYS_RETURN_STR
