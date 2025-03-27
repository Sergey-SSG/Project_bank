import json

import pandas as pd


def read_csv_file(file_path):
    """Считывает финансовые операции из CSV-файла."""
    try:
        data = pd.read_csv(file_path)
        print(f"Успешно считано {len(data)} записей из {file_path}.")
        return data.to_json(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None


def read_xlsx_file(file_path):
    """Считывает финансовые операции из XLSX-файла и возвращает список словарей"""

    try:
        data = pd.read_excel(file_path)
        print(f"Успешно считано {len(data)} записей из {file_path}.")
        return data.to_json(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None

if __name__ == '__main__':
    csv_file_path = "transactions.csv"
    xlsx_file_path = "transactions_excel.xlsx"
    print("\n")
    # Чтение данных из CSV
    csv_data = read_csv_file(csv_file_path)
    if csv_data is not None:
        print(csv_data)
    print("\n")
    # Чтение данных из XLSX
    xlsx_data = read_xlsx_file(xlsx_file_path)
    if xlsx_data is not None:
        print(xlsx_data)