from utils import arrs
import pytest



def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"

@pytest.mark.parametrize(
    ('coll', 'start', 'end', 'expected'),
    (
        ([1, 2, 3, 4], 1, 3, [2, 3]),
        ([1, 2, 3], 1, None, [2, 3]),
        ([1, 2, 3], 0, 3, [1, 2, 3]),
        ([1, 2, 3], None, 3, [1, 2, 3]),
        ([1, 2, 3], 1, 5, [2, 3]),
        ([], 1, 3, []),
        ([], None, None, []),
        ([1, 2, 3], None, None, [1, 2, 3]),
        ([], None, 3, []),
        ([], 3, None, []),
    )
)
def test_slice(coll, start, end, expected):
    if not start:
        assert arrs.my_slice(coll, None, end) == expected
    if not end:
        assert arrs.my_slice(coll, start) == expected
    elif end > len(coll):
        assert arrs.my_slice(coll, start, end) == expected
    if not coll:
        assert arrs.my_slice(coll, start, end) == expected