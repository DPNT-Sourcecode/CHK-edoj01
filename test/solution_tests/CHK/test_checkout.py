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