import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000  7** **** ***6 361"


@pytest.mark.parametrize(
    "card_number, expected_number",
    [
        (700079228960636112, "7000 79** **** **61 12"),
        (700079228960636, "7000 79** ***0 636"),
        ("700079228960636", "7000 79** ***0 636"),
        ("", ""),
        (" ", " "),
    ],
)
def test_get_mask_card_number_(card_number, expected_number):
    assert get_mask_card_number(card_number) == expected_number


def test_get_mask_account(mask_account):
    assert get_mask_account(mask_account) == "**4305"


@pytest.mark.parametrize(
    "account, expected_account",
    [
        (736541084301358743051, "**3051"),
        (7365410843013587430, "**7430"),
        ("1111111111111111", "**1111"),
        ("", "**"),
        (" ", "** "),
    ],
)
def test_get_mask_account_(account, expected_account):
    assert get_mask_account(account) == expected_account
