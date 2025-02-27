def get_primes_lower_n(n: int):
    def is_prime(num: int):
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    return [2] + [i for i in range(3, n + 1, 2) if is_prime(i)]


def get_maximum_power_lower_n(prime: int, n: int):
    result = prime
    while result * prime <= n:
        result *= prime
    return result


def get_lower_multiple(n: int):
    """
    Finds the smallest multiple of all numbers from 1 to n.
    """
    if isinstance(n, float):
        n = int(n)
    elif not isinstance(n, int):
        raise TypeError("you did not insert a number")
    if n < 1:
        raise ValueError("please insert a positive number")

    primes = get_primes_lower_n(n)

    result = 1

    for prime in primes:
        result *= get_maximum_power_lower_n(prime, n)
    return result


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

    # in real life I would do pytest.Raises
    has_raised_error = False
    message = ""
    try:
        get_lower_multiple("1345")
    except TypeError as e:
        message = str(e)
        has_raised_error = True

    assert has_raised_error, "when a string is passed it supposed to raise a TypeError"
    assert (
        message == "you did not insert a number"
    ), f"expected you did not insert a number as error message got {message}"

    has_raised_error = False
    message = ""
    try:
        get_lower_multiple(-234567.25)
    except ValueError as e:
        has_raised_error = True
        message = str(e)

    assert has_raised_error
    assert message == "please insert a positive number"

    has_raised_error = False
    message = ""
    try:
        get_lower_multiple(-234567)
    except ValueError as e:
        has_raised_error = True
        message = str(e)

    assert has_raised_error
    assert message == "please insert a positive number"
