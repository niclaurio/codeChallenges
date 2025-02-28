from typing import Any


def get_key_from_value(dictionary: dict, value: Any):
    """
    Ex:
        dictionary = {'a':1, 'b':2, 'c': 3}
        value = 3
        get_key_from_value(dictionary, value) returns 'c'
    """
    dict_values = list(dictionary.values())
    dict_keys = list(dictionary.keys())
    value_index = dict_values.index(value)
    return dict_keys[value_index]
