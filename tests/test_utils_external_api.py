from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub
from src.utils import load_transactions

# Тестирование функции load_transactions
# def test_load_transactions_valid_json() -> None:
#     mock_json_data = '[{"amount": 1000, "currency": "USD"}]'
#     with patch("builtins.open", mock_open(read_data=mock_json_data)):
#         result = load_transactions("dummy_path.json")
#
#     assert len(result) == 1
#     assert result[0]["amount"] == 1000
#     assert result[0]["currency"] == "USD"
#
#
# @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
# def test_load_transactions_success(mock_file):
#     result = load_transactions("dummy_path.json")
#     assert len(result) == 1
#     assert result[0]["amount"] == 100


def test_load_transactions_empty_file() -> None:

    with patch("builtins.open", mock_open(read_data="")):
        result = load_transactions("dummy_path.json")

    assert result == []


def test_load_transactions_invalid_json() -> None:
    mock_invalid_json = "{invalid json}"

    with patch("builtins.open", mock_open(read_data=mock_invalid_json)):
        result = load_transactions("dummy_path.json")

    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_load_transactions_invalid_json_(mock_file):
    result = load_transactions("dummy_path.json")
    assert result == []


def test_load_transactions_file_not_found() -> None:
    result = load_transactions("non_existent_file.json")
    assert result == []


@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_found_(mock_exists):
    result = load_transactions("dummy_path.json")
    assert result == []


# Тестирование функции convert_to_rub с использованием Mock API
@patch("src.external_api.requests.get")
def test_convert_to_rub_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75}}
    result = convert_to_rub(100, "result")
    assert result
