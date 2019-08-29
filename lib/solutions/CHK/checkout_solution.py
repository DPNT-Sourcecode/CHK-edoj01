from typing import Optional


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> Optional[int]:
    """Return -1 is sku is not a string.

    :param skus: Product skus for checkout
    :rtype: integer
    """
    if not isinstance(skus, str):
        return -1

