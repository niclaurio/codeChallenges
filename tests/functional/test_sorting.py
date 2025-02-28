from sorting import sorting
import pytest


def test_sorting():
    with pytest.raises(
        TypeError, match="Cannot sort: elements must be of the same type."
    ):
        sorting({1: "value", 2: 3.0, 3: "another"}, sort_by_key=False)

    with pytest.raises(
        TypeError, match="Cannot sort: elements must be of the same type."
    ):
        sorting([1, "string", 3.14])

    with pytest.raises(
        TypeError, match="Cannot sort: elements must be of the same type."
    ):
        sorting({"a": 1, 2: 3})

    my_int_list = [9, 1, 8, 2, 7, 3, 6, 4, 5]

    res1 = sorting(my_int_list)
    assert res1 == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ], f"expected [1,2,3,4,5,6,7,8,9] got {res1}"

    res2 = sorting(my_int_list, reverse=True)
    assert res2 == [
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1,
    ], f"expected [9,8,7,6,5,4,3,2,1] got {res2}"

    my_float_list = [3.4, 1.25, -4.768, 34, -67.65, -12]

    res3 = sorting(my_float_list)
    assert res3 == [-67.65, -12, -4.768, 1.25, 3.4, 34]
