from typing import List


def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def sorting_decorator(func):
    def wrapper(vals, *args, reverse=False, **kwargs):
        if not vals:
            raise ValueError("Cannot sort an empty list or dictionary.")
        if not has_only_one_datatype(vals):
            raise TypeError("Cannot sort: elements must be of the same type.")
        if isinstance(vals, list) and type(vals[0]) not in (float, str, int):
            raise TypeError(
                "Only lists or dictionaries with integers, floats, or strings can be sorted."
            )

        result = func(vals, *args, **kwargs)
        return result[::-1] if reverse else result

    return wrapper


@sorting_decorator
def sorting(vals: list | dict, by_key=True, reverse: bool = False) -> list | dict:
    """
    Sorts a list or dictionary (by keys or values) using the Quicksort algorithm.

    Only lists and dictionaries can be sorted:
    - Strings and tuples are immutable, so sorting in place is impossible.
    - Integers and floats are not iterable.
    - Sets are unordered and cannot be sorted directly.

    Args:
        vals (list | dict): The list or dictionary to be sorted.
        by_key (bool, optional): When sorting dictionaries, determines whether to sort by keys (True) or values (False). Defaults to True.
        reverse(bool, optional): Whether to sort in descending (True) or ascending(False) order
    Returns:
        list | dict: The sorted list or dictionary.

    Raises:
        ValueError: If the input list or dictionary is empty.
        TypeError: If elements in the list or dictionary keys/values have mixed types or unsupported types.
    """

    def get_dictionary_by_values(values):
        keys = list(vals.keys())
        return {keys[i]: val for i, val in enumerate(values)}

    if isinstance(vals, dict):
        values_to_sort = list(vals.keys()) if by_key else list(vals.values())
        sorted_vals = quicksort(values_to_sort)
        sorted_vals = sorted_vals if not reverse else sorted_vals[::-1]
        return (
            {el: vals[el] for el in sorted_vals}
            if by_key
            else get_dictionary_by_values(sorted_vals)
        )

    if isinstance(vals, list):
        sorted_vals = quicksort(vals)
        return sorted_vals if not reverse else sorted_vals[::-1]

    raise TypeError("Invalid input type: only lists and dictionaries are supported.")


def has_only_one_datatype(vals: List) -> bool:
    return len({type(el) for el in vals}) == 1
