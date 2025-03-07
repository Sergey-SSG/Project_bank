import pytest


# Фикстура модуля masks.py
@pytest.fixture
def card_number():
    return "7000 79** **** 6361"


# Фикстура модуля masks.py
@pytest.fixture
def mask_account():
    return "**4305"


# Фикстура модуля processing.py
@pytest.fixture
def dates():
    return []


# Фикстура модуля widget.py
@pytest.fixture
def date():
    return "11.03.2024"

