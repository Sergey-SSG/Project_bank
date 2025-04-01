import pytest
from src.transactions import find_transactions_by_description
from src.transactions import count_transaction_categories


def test_find_transactions_by_description_found(TRANSACTIONS):
    """Тест, когда строка поиска находится в описании."""
    results = find_transactions_by_description(TRANSACTIONS, 'покупка')
    assert len(results) == 2
    assert results[0]['id'] == 1
    assert results[1]['id'] == 5


def test_find_transactions_by_description_not_found(TRANSACTIONS):
    """Тест, когда строка поиска не найдена."""
    results = find_transactions_by_description(TRANSACTIONS, 'несуществующее')
    assert len(results) == 0


def test_find_transactions_by_description_case_insensitive(TRANSACTIONS):
    """Тест на регистронезависимость поиска."""
    results = find_transactions_by_description(TRANSACTIONS, 'ПОКУПКА')
    assert len(results) == 2
    assert results[0]['id'] == 1
    assert results[1]['id'] == 5


def test_find_transactions_by_description_empty_search_string(TRANSACTIONS):
    """Тест с пустой строкой поиска."""
    results = find_transactions_by_description(TRANSACTIONS, '')
    assert len(results) == 6  # Возвращает все, так как пустая строка есть везде


def test_find_transactions_by_description_no_description_key(TRANSACTIONS):
    """Тест когда в транзакции нет ключа 'description'."""
    results = find_transactions_by_description(TRANSACTIONS, 'test')
    assert len(results) == 0  # Не должно вызывать исключение


def test_count_transaction_categories_basic(TRANSACTIONS):
    """Тест с базовым набором транзакций."""
    category_counts = count_transaction_categories(TRANSACTIONS)
    assert category_counts['Покупка в магазине "Пятерочка"'] == 1
    assert category_counts['Оплата интернета'] == 1
    assert category_counts['Перевод другу'] == 1
    assert category_counts[''] == 1  # Проверка на транзакцию без description


def test_count_transaction_categories_empty_list(TRANSACTIONS):
    """Тест с пустым списком транзакций."""
    category_counts = count_transaction_categories([])
    assert category_counts == {}


def test_count_transaction_categories_all_same(TRANSACTIONS):
    """Тест, когда все транзакции имеют одинаковое описание."""
    transactions = [{'id': i, 'description': 'Одинаковое описание'} for i in range(6)]
    category_counts = count_transaction_categories(transactions)
    assert category_counts['Одинаковое описание'] == 6


def test_count_transaction_categories_no_description(TRANSACTIONS):
    """Тест, когда у всех транзакций отсутствует описание."""
    transactions = [{'id': i} for i in range(3)]
    category_counts = count_transaction_categories(transactions)
    assert category_counts[''] == 3
