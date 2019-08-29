"""
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""
from solutions.CHK import checkout_solution
from hypothesis import given
from hypothesis.strategies import integers



def test_checkout():
    assert checkout_solution.checkout("ABCD") == 4


def test_sum_of_sku():
    assert checkout_solution.sum_of_sku(1,1,1,1) == 0


def test_calcATotal():
    assert checkout_solution.calcATotal(1) == 0


def test_calcBTotal():
    assert checkout_solution.calcBTotal(1) == 0

