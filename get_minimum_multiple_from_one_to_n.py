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

        The algorithm multiplies the highest power of each prime number less than or equal to n.

        Args:
            n (int): The upper limit up to which we want to find the smallest multiple.

        Returns:
            int: The smallest multiple that is divisible by all numbers from 1 to n.

        Raises:
            TypeError: If n is not an integer.
            ValueError: If n is less than 1.
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
