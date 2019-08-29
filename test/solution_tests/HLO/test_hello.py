from solutions.HLO import hello_solution
import pytest


possible_friends = [["John", "Hello, John!"],]

@pytest.mark.parametrize("test_name,test_greeting", possible_friends)
def test_hello(test_name, test_greeting):
    assert hello_solution.hello(test_name) == test_greeting
