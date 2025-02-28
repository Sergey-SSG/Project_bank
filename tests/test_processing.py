import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    assert filter_by_state([], "") == []
    # with pytest.raises(ValueError):
    #     filter_by_state('', '') == []


@pytest.mark.parametrize(
    "value, expected",
    [
        ([], []),
        ([], []),
    ],
)
def test_filter_by_state(value, expected):
    assert filter_by_state(value) == expected


def test_sort_by_date():
    assert sort_by_date([], 0) == []
    # with pytest.raises(ValueError):
    #     sort_by_date('', 0) == []


def test_sort_by_date(dates):
    assert sort_by_date([], 0) == dates
