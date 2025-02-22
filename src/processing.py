from datetime import datetime
from typing import Iterable


def filter_by_state(data: Iterable[list], state="EXECUTED") -> list:
    """Функция ринимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: Iterable[list], descending=True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)"""
    return sorted(
        data,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=descending,
    )
