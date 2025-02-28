from typing import List


def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def sorting(
    values: list | dict, sort_by_key=True, reverse: bool = False
) -> list | dict:
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

    def sort_dict_by_values(sorted_values):
        value_list = list(values.values())
        key_list = list(values.keys())
        sorted_dict = {}
        for val in sorted_values:
            val_index = value_list.index(val)
            key = key_list[val_index]
            sorted_dict[key] = val
        return sorted_dict

    if not isinstance(values, (list, dict)):
        raise TypeError(
            "Invalid input type: only lists and dictionaries are supported."
        )

    if not values:
        raise ValueError("Cannot sort an empty list or dictionary.")

    elements_to_sort = (
        values
        if isinstance(values, list)
        else list(values.keys()) if sort_by_key else list(values.values())
    )

    if not has_only_one_datatype(elements_to_sort):
        raise TypeError("Cannot sort: elements must be of the same type.")

    if type(elements_to_sort[0]) not in (float, str, int):
        raise TypeError(
            "Only lists or dictionaries with integers, floats, or strings can be sorted."
        )

    sorted_elements = quicksort(elements_to_sort)
    sorted_elements = sorted_elements if not reverse else sorted_elements[::-1]
    if isinstance(values, dict):
        return (
            {key: values[key] for key in sorted_elements}
            if sort_by_key
            else sort_dict_by_values(sorted_elements)
        )

    return sorted_elements


def has_only_one_datatype(vals: List) -> bool:
    types = {type(el) for el in vals}
    if int in types and float in types and len(types) == 2:
        return True
    return len(types) == 1
