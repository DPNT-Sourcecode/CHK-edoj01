from solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout("ABCD") == 115
    assert checkout_solution.checkout("ABCDE") == 155
    assert checkout_solution.checkout("ABCDEF") == 165
    assert checkout_solution.checkout("ABCDEFG") == 185
    assert checkout_solution.checkout("ABC4") == -1
    assert checkout_solution.checkout("CXYZYZC") == 105
    assert checkout_solution.checkout("K") == 80
    assert checkout_solution.checkout("S") == 20

def test_sum_of_sku():
    assert checkout_solution.sum_of_sku(1,1,1,1) == 1


def test_calcATotal():
    assert checkout_solution.calcATotal(1) == 50
    assert checkout_solution.calcATotal(7) == 300


def test_calcBTotal():
    assert checkout_solution.calcBTotal(1) == 30
    assert checkout_solution.calcBTotal(13) == 300

def test_calcFTotal():
    assert checkout_solution.calcFTotal(1) == 10
    assert checkout_solution.calcFTotal(9) == 60


def test_calc_stxyz():
    assert checkout_solution.calc_stxyz("STY") == 45
    assert checkout_solution.calc_stxyz("S") == 20
    assert checkout_solution.calc_stxyz("STYXZ") == 72
    assert checkout_solution.calc_stxyz("STYXZTUUU") == 90
