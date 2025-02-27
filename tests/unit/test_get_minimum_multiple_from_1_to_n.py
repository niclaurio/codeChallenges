from get_minimum_multiple_from_one_to_n import get_primes_lower_n, get_maximum_power_lower_n, get_lower_multiple
import pytest
from unittest.mock import call

def test_get_primes_lower_n():
    res = get_primes_lower_n(12)
    assert res == [2, 3,5,7,11], f"expected [2,3,5,7,11] got {res}"

    res2 = get_primes_lower_n(23)
    assert res2 == [2,3,5,7,11,13,17,19,23], f"expected [2,3,5,7,11,13,17,19,23] got {res2}"

    res3 = get_primes_lower_n(49)
    expected_res_3 =  [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    assert res3 ==expected_res_3, f"expected {expected_res_3} got {res3}"


def test_get_maximum_power_lower_n():
    res = get_maximum_power_lower_n(3, 92)
    assert res == 81, f"expected 81 got {res}"

    res2 = get_maximum_power_lower_n(5, 125)
    assert res2 == 125, f"expected 125 got {res2}"

@pytest.fixture
def mock_get_primes_lower_n(mocker):
    mock = mocker.patch('get_minimum_multiple_from_one_to_n.get_primes_lower_n')
    mock.side_effect = lambda n : [2,3,5,7] if n == 10 else [2,3,5,7,11,13,17,19]
    return mock

@pytest.fixture
def mock_get_maximum_power_lower_n(mocker):
    def get_power(prime, n):
        power_of_2 = 8 if n == 10 else 16
        return power_of_2 if prime == 2 else 9 if prime == 3 else prime
    mock = mocker.patch('get_minimum_multiple_from_one_to_n.get_maximum_power_lower_n')
    mock.side_effect = lambda prime, n: get_power(prime, n)
    return mock

@pytest.mark.parametrize(
    "n, expected_result", [
        (10, 2520),
        (20, 2520*11*13*17*19*2)
    ]
)
def test_get_lower_multiple(mock_get_primes_lower_n, mock_get_maximum_power_lower_n, n, expected_result):
    result = get_lower_multiple(n)
    assert result == expected_result, f"expected {expected_result} got {result}"

    mock_get_primes_lower_n.assert_called_once_with(n)

    calls = [
        call(2,n),
        call(3,n),
        call(5, n),
        call(7, n)
    ]
    if n == 20:
        calls.extend(
            [
                call(11, n),
                call(13, n),
                call(17, n),
                call(19,n)
            ]
        )
    mock_get_maximum_power_lower_n.assert_has_calls(calls, any_order=False)


