from sorting import sorting, quicksort, has_only_one_datatype
import pytest


def test_quicksort():
    res1 = quicksort([9, 1, 8, 2, 7, 3, 6, 4, 5])
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
    ], f"expected [1,2,3,4,5,6,7,8,9] got {res1} "

    res2 = quicksort([6.9, -2.75, 5.8, -1.654, 4.7, 0.5, 3.0134, 1.4, 2.12])
    assert res2 == [
        -2.75,
        -1.654,
        0.5,
        1.4,
        2.12,
        3.0134,
        4.7,
        5.8,
        6.9,
    ], f"expected [-2.75, -1.654, 0.5, 1.4, 2.12, 3.0134, 4.7, 5.8, 6.9] got {res2} "

    res3 = quicksort(["e", "a", "d", "b", "c"])
    assert res3 == ["a", "b", "c", "d", "e"]

    res4 = quicksort([6.9, 4, 12.6, -5])
    assert res4 == [-5, 4, 6.9, 12.6]


def test_has_only_one_data_type():
    assert has_only_one_datatype([1, 2, 3, 4, 5, 6, 7, 8])
    assert not has_only_one_datatype([1, 2, 3, 4, 5, "a"])
    assert has_only_one_datatype([1, 2, 3, 3.6789])
    assert not has_only_one_datatype([1, "3,678", 4.567])


@pytest.fixture
def mock_quicksort(mocker):
    mock = mocker.patch("sorting.quicksort")
    return mock


@pytest.fixture
def mock_has_only_one_datatype(mocker):
    mock = mocker.patch("sorting.has_only_one_datatype")
    return mock


def test_sorting(mock_quicksort, mock_has_only_one_datatype):
    mock_has_only_one_datatype.return_value = False
    with pytest.raises(ValueError, match="Cannot sort an empty list or dictionary."):
        sorting([])

    with pytest.raises(ValueError, match="Cannot sort an empty list or dictionary."):
        sorting({})

    with pytest.raises(
        TypeError,
        match="Invalid input type: only lists and dictionaries are supported.",
    ):
        sorting(42)

    with pytest.raises(
        TypeError,
        match="Invalid input type: only lists and dictionaries are supported.",
    ):
        sorting((1, 2, 4))

    with pytest.raises(
        TypeError,
        match="Invalid input type: only lists and dictionaries are supported.",
    ):
        sorting({1, 2, 4})

    with pytest.raises(
        TypeError,
        match="Invalid input type: only lists and dictionaries are supported.",
    ):
        sorting("pluto")

    with pytest.raises(
        TypeError, match="Cannot sort: elements must be of the same type."
    ):
        sorting([1, 2, 3, 4, "5"])
    mock_has_only_one_datatype.return_value = True
    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting([{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}])

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting([{"a": 1, "b": 2}, {"c": 3, "d": 4}])

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting(
            {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8], "c": [9, 10, 11, 12]},
            sort_by_key=False,
        )

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting(
            {"a": (1, 2, 3, 4), "b": (5, 6, 7, 8), "c": (9, 10, 11, 12)},
            sort_by_key=False,
        )

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting(
            {"a": {1, 2, 3, 4}, "b": {5, 6, 7, 8}, "c": {9, 10, 11, 12}},
            sort_by_key=False,
        )

    with pytest.raises(
        TypeError,
        match="Only lists or dictionaries with integers, floats, or strings can be sorted.",
    ):
        sorting({"a": {"b": 1, "c": 2}, "d": {"e": 3, "f": 4}}, sort_by_key=False)

    quick_sort_returned_value = list(range(1, 6))
    reversed_quick_sort_returned_value = sorted(quick_sort_returned_value, reverse=True)
    mock_quicksort.return_value = quick_sort_returned_value

    # list test

    vals_list = [5, 1, 4, 2, 3]
    assert (
        sorting(vals_list) == quick_sort_returned_value
    ), f"expected {quick_sort_returned_value}, got {sorting(vals_list) }"  # ascending sorting
    assert (
        sorting(vals_list, reverse=True) == reversed_quick_sort_returned_value
    )  # descending sorting

    # sorting dictionary values
    vals_dict = {"a": 5, "b": 1, "c": 4, "d": 2, "e": 3}
    assert sorting(vals_dict, sort_by_key=False) == {
        "b": 1,
        "d": 2,
        "e": 3,
        "c": 4,
        "a": 5,
    }  # ascending sorting
    assert sorting(vals_dict, sort_by_key=False, reverse=True) == {
        "a": 5,
        "c": 4,
        "e": 3,
        "d": 2,
        "b": 1,
    }  # descending sorting

    # sorting dictionary keys
    vals_dict = {5: "a", 1: "b", 4: "c", 2: "d", 3: "e"}
    assert sorting(vals_dict) == {1: "b", 2: "d", 3: "e", 4: "c", 5: "a"}
    assert sorting(vals_dict, reverse=True) == {5: "a", 4: "c", 3: "e", 2: "d", 1: "b"}
