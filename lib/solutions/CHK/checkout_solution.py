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

def sum_value_of_a(num_a:int) -> int:
    specials, whole_price = divmod(num_a, 3)
    return (specials * 130) + (whole_price * 50) 

def sum_of_sku(
    num_items: int,
    price: int,
    special_vol: int=None,
    special_price: int=None
):
    specials, whole_price = divmod(num_items, special_vol)
    return (specials * special_price) + (whole_price * price)



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> Optional[int]:
    """Return -1 is sku is not a string.

    :param skus: Product skus for checkout
    :rtype: integer
    """

    if not isinstance(skus, str):
        return -1


