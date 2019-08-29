from collections import Counter
from typing import Optional
import attr


NO_DISCOUNT_SKUS = [
  ["C", 20],
  ["D", 15],
  ["G", 20],
  ["I", 35],
  ["J", 60],
  ["L", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
  ["C", 20],
]

CROSS_ITEM_DISCOUNTS_CONF = [
  ["E", 2, "B", 1],
  ["N", 3, "M", 1],
  ["R", 3, "Q", 1],
]



def sum_of_sku(
    num_items: int,
    price: int,
    special_vol: int=None,
    special_price: int=None
) -> int:
    """Calculate the total owed for the number of items of a given item
    in the skus arg.

    :param num_items: count of item
    :param price: the whole item price of the individual items
    :param special_vol: the volume required to qualify for discount
    :param special_price: the price for a discount
    :returns: total price for the items of SKU
    :rtype integer:
    """
    specials, whole_price = divmod(num_items, special_vol)
    return (specials * special_price) + (whole_price * price)


def calcATotal(num_as: int) -> int:
    """Return total owed for A SKU from volume"""
    biggest_discount_vol, remainder = divmod(num_as, 5)
    value = biggest_discount_vol * 200
    return value + sum_of_sku(remainder, 50, 3, 130)


def calcBTotal(num_bs: int) -> int:
    """Return total owed for B SKU from volume"""
    return sum_of_sku(num_bs, 30, 2, 45)


def calcFTotal(num_fs: int) -> int:
    """Return total owed for F SKU from volume"""
    return sum_of_sku(num_fs, 10, 3, 20)


def calcHTotal(num_hs: int) -> int:
    """Return total owed for H SKU from volume"""
    biggest_discount_vol, remainder = divmod(num_hs, 10)
    value = biggest_discount_vol * 80
    return value + sum_of_sku(remainder, 10, 5, 45)


def calcKTotal(num_ks: int) -> int:
    """Return total owed for H SKU from volume"""
    return sum_of_sku(num_ks, 80, 2, 150)


def calcPTotal(num_ps: int) -> int:
    """Return total owed for P SKU from volume"""
    return sum_of_sku(num_ps, 50, 5, 200)


def calcQTotal(num_qs: int) -> int:
    """Return total owed for Q SKU from volume"""
    return sum_of_sku(num_ps, 30, 3, 80)


def calcUTotal(num_us: int) -> int:
    """Return total owed for F SKU from volume"""
    return sum_of_sku(num_us, 40, 3, 80)


def calcVTotal(num_vs: int) -> int:
    """Return total owed for H SKU from volume"""
    biggest_discount_vol, remainder = divmod(num_vs, 3)
    value = biggest_discount_vol * 130
    return value + sum_of_sku(remainder, 50, 2, 90)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> Optional[int]:
    """Return -1 is sku is not a string.

    :param skus: Product skus for checkout
    :return: Total value of basket
    :rtype: integer
    """
    total_value = 0
    basket = Counter(skus)

    # Add all totals for valid SKUs
    total_value += calcATotal(basket.pop("A", 0))
    total_value += calcFTotal(basket.pop("F", 0))
    total_value += basket.pop("C", 0) * 20
    total_value += basket.pop("D", 0) * 15
    e_vol = basket.pop("E", 0)
    total_value += e_vol * 40

    basket["B"] = max(0, basket.get("B", 0) - divmod(e_vol, 2)[0])
    total_value += calcBTotal(basket.pop("B", 0))
    # Return -1 if there are any SKUs that remain
    if basket:
        return -1

    return total_value


