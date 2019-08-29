from typing import Optional
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
    if special_vol is not None:
        specials, whole_price = divmod(num_items, special_vol)
        return (specials * special_price) + (whole_price * price)


def calcATotal(num_as: int) -> int:
    """Return total owed for A SKU from volume"""
    return sum_of_sku(num_as, 50, 3, 130)


def calcBTotal(num_bs: int) -> int:
    """Return total owed for B SKU from volume"""
    return sum_of_sku(num_bs, 30, 2, 45)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> Optional[int]:
    """Return -1 is sku is not a string.

    :param skus: Product skus for checkout
    :rtype: integer
    """
    A_vol = 

    if not isinstance(skus, str):
        return -1
