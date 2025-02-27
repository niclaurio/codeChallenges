from typing import Tuple


def get_reversed_string(my_string: str) -> str:
    return my_string[::-1]


def is_palindrome(text: str) -> Tuple[bool, str]:
    """
    EX:
        is_palindrome('Francesco') returns False
        is_palindrome('ANNA') returns True
    """

    if not isinstance(text, str):
        raise TypeError("you did not insert a string")
    return get_reversed_string(text) == text

