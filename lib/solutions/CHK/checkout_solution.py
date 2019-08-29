from collections import Counter
from typing import Optional
import attr


NO_DISCOUNT_SKUS = [
  ["C", 20],
  ["D", 15],
  ["G", 20],
  ["I", 35],
  ["J", 60],
  ["L", 90],
  ["M", 15],
  ["O", 10],
  ["W", 20],
  ["E", 40],
  ["N", 40],
  ["R", 50],
]


CROSS_ITEM_DISCOUNTS_CONF = [
  ["E", 2, "B", 1],
  ["N", 3, "M", 1],
  ["R", 3, "Q", 1],
]

STXYZ_PRICE = {
  "Z": 21,
  "S": 20,
  "T": 20,
  "X": 17,
  "Y": 20,
}


def calc_stxyz(skus):
    prices = [STXYZ_PRICE[sku] for sku in skus if sku in STXYZ_PRICE]
    prices.sort(reverse=True)
    num_in_discount = len(prices)
    if num_in_discount < 3:
        return sum(prices)
    total_discount = divmod(num_in_discount, 3)[0]
    return (total_discount * 45) + sum(prices[total_discount * 3:])


def apply_discounts(basket):
    for item, vol, discount_item, discount_vol in CROSS_ITEM_DISCOUNTS_CONF:
        to_discount = divmod(basket.get(item, 0), vol)[0]
        basket[discount_item] = max(
            0,
            basket.get(discount_item, 0) - to_discount
        )

    return basket


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
    return sum_of_sku(num_ks, 70, 2, 120)


def calcPTotal(num_ps: int) -> int:
    """Return total owed for P SKU from volume"""
    return sum_of_sku(num_ps, 50, 5, 200)


def calcQTotal(num_qs: int) -> int:
    """Return total owed for Q SKU from volume"""
    return sum_of_sku(num_qs, 30, 3, 80)


def calcUTotal(num_us: int) -> int:
    """Return total owed for F SKU from volume"""
    return sum_of_sku(num_us, 40, 4, 120)


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
    total_value = calc_stxyz(skus)
    basket = Counter(skus)
    basket = apply_discounts(basket)
    for sku in STXYZ_PRICE.keys():
        basket.pop(sku, 0)

    total_value += sum(basket.pop(sku, 0) * sku_price for sku, sku_price in NO_DISCOUNT_SKUS)

    if not basket:
        return total_value

    # Add all totals for valid SKUs
    total_value += calcATotal(basket.pop("A", 0))
    total_value += calcBTotal(basket.pop("B", 0))
    total_value += calcFTotal(basket.pop("F", 0))
    total_value += calcHTotal(basket.pop("H", 0))
    total_value += calcKTotal(basket.pop("K", 0))
    total_value += calcPTotal(basket.pop("P", 0))
    total_value += calcQTotal(basket.pop("Q", 0))
    total_value += calcUTotal(basket.pop("U", 0))
    total_value += calcVTotal(basket.pop("V", 0))

    # Return -1 if there are any SKUs that remain
    if basket:
        return -1

    return total_value



