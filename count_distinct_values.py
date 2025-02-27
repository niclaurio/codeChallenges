from typing import Iterable


def count_values(vals: Iterable) -> dict[str, int]:
    """
    it calculates how many times each element is repeated
    """
    distinct_vals = set(vals)
    return {str(val): vals.count(val) for val in distinct_vals}

