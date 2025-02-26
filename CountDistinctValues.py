from typing import Iterable


def count_values(vals: Iterable) -> dict[str, int]:
    """
    it calculates how many times each element is repeted
    """
    distinct_vals = set(vals)
    return {str(val):vals.count(val) for val in distinct_vals}


def test_count_values():
    sentence = "Anna ama mangiare ananas ama anche andare al mare e ammirare le onde"
    expected_res1 = count_values(sentence)
    res = {'a': 17, ' ': 12, 'n': 8, 'e': 8, 'm': 6, 'r': 5, 'i': 2, 'd': 2, 'l': 2, 'A': 1, 'g': 1, 's': 1, 'c': 1, 'h': 1, 'o': 1}
    assert len(res) == len(expected_res1), f"expected {len(res)} distinct values got {len(expected_res1)}"
    assert isinstance(expected_res1, dict), f"expected dict as returning type got {type(expected_res1)}"
    for el, val in expected_res1:
        assert res[el] == val , f "expected {el} to be repeated {val} times, got {res[el]}"

    expected_res2 = count_values(list(sentence))
    assert len(res) == len(expected_res2), f"expected {len(res)} distinct values got {len(expected_res2)}"
    assert isinstance(expected_res2, dict), f"expected dict as returning type got {type(expected_res2)}"
    for el, val in expected_res2:
        assert res[el] == val , f "expected {el} to be repeated {val} times, got {res[el]}"
   
