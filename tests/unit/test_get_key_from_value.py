from get_key_from_value import get_key_from_value


def test_get_key_from_value():
    dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 4}
    expected_res_1 = "c"
    res_1 = get_key_from_value(dictionary, 3)
    assert res_1 == expected_res_1, f"expected {expected_res_1}, got {res_1}"

    expected_res_2 = "d"
    res_2 = get_key_from_value(dictionary, 4)
    assert res_2 == expected_res_2, f"expected {expected_res_2} got {res_2}"