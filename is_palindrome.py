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

    message=''
    has_raised_error = False
    try:
        is_palindrome('AnnA1')
    except TypeError as e:
        has_raised_error = True
        message = str(e)
    assert has_raised_error
    assert message == "you did not insert a valid string format"