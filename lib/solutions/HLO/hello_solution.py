ALWAYS_RETURN_TMP = "Hello, {name}!" 
"""Constant template to expand the hello greeting
"""

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str):
    """Some hello message that completely ignores the parameter.

    :param friend_name: the name of the friend to greet
    :type friend_name: string
    :rtype: str
    """
    return ALWAYS_RETURN_TMP.format(name=friend_name)
