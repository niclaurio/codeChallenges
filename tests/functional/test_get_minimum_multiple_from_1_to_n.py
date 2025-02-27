from get_minimum_multiple_from_one_to_n import get_lower_multiple
import pytest

def test_get_lower_multiple():
    res1 = get_lower_multiple(10)
    assert res1 == 2520, f"expected 2520 got {res1}"

    res2 = get_lower_multiple(9)
    assert res1 == res2, f"expected 2520 got {res2}"

    res3 = get_lower_multiple(25)
    assert (
        res3 == 16 * 9 * 25 * 7 * 11 * 13 * 17 * 19 * 23
    ), f"expected {16 * 9 * 25 * 7 * 11 * 13 * 17 * 19 * 23} got {res3}"

    res4 = get_lower_multiple(12.897)
    assert res4 == 2520 * 11, f"expected {2520*11} got {res4}"

    with pytest.raises(TypeError) as exc_info:
        get_lower_multiple("1345")
        assert str(exc_info) == "you did not insert a number"

    with pytest.raises(ValueError) as exc_info:
        get_lower_multiple(-234567.25)
        assert str(exc_info) == "please insert a positive number"

    with pytest.raises(ValueError) as exc_info:
        get_lower_multiple(-234567)
        assert str(exc_info) == "please insert a positive number"

