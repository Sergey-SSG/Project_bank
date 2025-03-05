import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    assert filter_by_state([], "") == []
    # with pytest.raises(ValueError):
    #     filter_by_state('', '') == []

@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ([], []),
        ([], []),
    ],
)
def test_filter_by_state_(value, expected):
    assert filter_by_state(value) == expected


def test_sort_by_date():
    assert sort_by_date([], 0) == []
    # with pytest.raises(ValueError):
    #     sort_by_date('', 0) == []


def test_sort_by_date_(dates):
    assert sort_by_date([], 0) == dates
