from unittest.mock import patch

import pandas as pd

from src.csv_xlsx_file import read_csv_file, read_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file_success(mock_read_csv):
    # Настройка Mock-объекта для возвращаемых данных
    mock_data = pd.DataFrame(
        {"date": ["2023-01-01", "2023-01-05"], "description": ["Salary", "Groceries"], "amount": [5000, -150]}
    )
    mock_read_csv.return_value = mock_data

    result = read_csv_file("test.csv")

    assert result is not None
    assert len(result) == 2
    assert result["description"][0] == "Salary"


@patch("pandas.read_csv")
def test_read_csv_file_failure(mock_read_csv):
    # Настройка Mock-объекта для генерации исключения
    mock_read_csv.side_effect = Exception("File not found")

    result = read_csv_file("test.csv")

    assert result is None


@patch("pandas.read_excel")
def test_read_xlsx_file_success(mock_read_excel):
    # Настройка Mock-объекта для возвращаемых данных
    mock_data = pd.DataFrame(
        {"date": ["2023-01-01", "2023-01-05"], "description": ["Salary", "Groceries"], "amount": [5000, -150]}
    )
    mock_read_excel.return_value = mock_data

    result = read_xlsx_file("test.xlsx")

    assert result is not None
    assert len(result) == 2
    assert result["description"][0] == "Salary"


@patch("pandas.read_excel")
def test_read_xlsx_file_failure(mock_read_excel):
    # Настройка Mock-объекта для генерации исключения
    mock_read_excel.side_effect = Exception("File not found")

    result = read_xlsx_file("test.xlsx")

    assert result is None
