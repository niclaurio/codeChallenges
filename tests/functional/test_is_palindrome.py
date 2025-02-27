from is_palindrome import is_palindrome
import pytest

def test_is_palindrome():
    with pytest.raises(TypeError) as exc_info:
        is_palindrome(['1', '2', '1'])
        assert str(exc_info) == 'you did not insert a string'

    assert is_palindrome('anna')
    assert not is_palindrome('Anna')
    assert is_palindrome('AnnA')
    assert is_palindrome('aNNa')
    assert not is_palindrome('francesco')
