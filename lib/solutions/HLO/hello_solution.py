ALWAYS_RETURN_STR= "Hello, World!" 

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str):
    """Some hello message that completely ignores the parameter.

    :param friend_name: undefined
    :type friend_name: string
    :rtype: int
    """
    return ALWAYS_RETURN_STR
