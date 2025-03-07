from datetime import datetime
from typing import Any


def filter_by_state(data: Any, state: str = "EXECUTED") -> list[dict]:
    """Функция ринимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: Any, descending: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)"""
    return sorted(
        data,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=descending,
    )


if __name__ == "__main__":
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(data))
    print(sort_by_date(data))
