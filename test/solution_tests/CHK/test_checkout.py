from solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout("ABCD") == 115
    assert checkout_solution.checkout("ABCDE") == -1



def test_sum_of_sku():
    assert checkout_solution.sum_of_sku(1,1,1,1) == 1


def test_calcATotal():
    assert checkout_solution.calcATotal(1) == 50
    assert checkout_solution.calcATotal(7) == 310


def test_calcBTotal():
    assert checkout_solution.calcBTotal(1) == 30
    assert checkout_solution.calcBTotal(13) == 300



