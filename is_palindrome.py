from typing import Tuple

def get_reversed_string(my_string: str) -> str:
    return my_string[::-1]

def is_palindrome(text: str) -> Tuple[bool, str]:
    """
    EX:
        is_palindrome('Francesco') returns False
        is_palindrome('ANNA') returns True
    """

    if not text.isalpha():
        raise TypeError("you did not insert a valid string format")
    return get_reversed_string(text) == text


def test_get_reversed_string():
    res =  get_reversed_string('pippo')
    assert res == 'oppip', f"expected oppip , got {res}"


def test_is_palindrome():
    assert is_palindrome('ANNA')
    assert not is_palindrome('aNNA')
    assert is_palindrome('aNNa')
    assert not is_palindrome('francesco')
