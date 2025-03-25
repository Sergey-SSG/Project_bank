import pandas as pd


def read_csv_file(file_path):
    """Считывает финансовые операции из CSV-файла."""
    try:
        data = pd.read_csv(file_path)
        print(f"Успешно считано {len(data)} записей из {file_path}.")
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None


def read_xlsx_file(file_path):
    """Считывает финансовые операции из XLSX-файла."""
    try:
        data = pd.read_excel(file_path)
        print(f"Успешно считано {len(data)} записей из {file_path}.")
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None
