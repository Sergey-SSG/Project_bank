import re
from collections import Counter
from typing import List, Dict

transactions = [
    {'id': 1, 'description': 'Покупка в магазине "Пятерочка"'},
    {'id': 2, 'description': 'Оплата интернета'},
    {'id': 3, 'description': 'Пополнение счета'},
    {'id': 4, 'description': 'Перевод другу'},
]


def find_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Находит транзакции, в описании которых содержится заданная строка (игнорируя регистр).
    Args:
        transactions: Список словарей с данными о банковских операциях. Каждый словарь должен иметь ключ 'description'.
        search_string: Строка для поиска в описании транзакций.
    Returns:
        Список словарей с транзакциями, у которых в описании есть заданная строка.
    """
    # 1
    # results: List[Dict] = []
    # for transaction in transactions:
    #     description = transaction.get('description', '') # Безопасное получение значения, если ключа нет
    #     if re.search(search_string, description, re.IGNORECASE):
    #         results.append(transaction)
    # return results

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_transaction_categories(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по каждой категории на основе поля 'description'.
    Args:
        transactions: Список словарей с данными о банковских операциях. Каждый словарь должен иметь ключ 'description'.
    Returns:
        Словарь, в котором ключи - это названия категорий (значения поля 'description'), а значения - количество операций в каждой категории.
    """
    # 1
    descriptions = [transaction.get('description', '') for transaction in
                    transactions]  # Безопасное получение, пустая строка, если нет ключа
    category_counts = Counter(descriptions)
    return dict(category_counts)
    # 2
    # categories = [transaction.get('description', '').lower() for transaction in transactions]
    # return dict(Counter(categories))
    # 3
    # counts = Counter(tx['description'] for tx in transactions if tx['description'])
    # return dict(counts)

if __name__ == '__main__':
    search_string = "покупка"
    found_transactions = find_transactions_by_description(transactions, search_string)

    for transaction in found_transactions:
        print(transaction)

    category_counts = count_transaction_categories(transactions)
    print(category_counts)
