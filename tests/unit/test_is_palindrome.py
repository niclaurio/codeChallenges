from is_palindrome import get_reversed_string


def test_get_reversed_string():
    res = get_reversed_string("pippo")
    assert res == "oppip", f"expected oppip , got {res}"
