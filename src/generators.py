from typing import Any, Generator


def filter_by_currency(transactions: Any, code: str) -> list:
    """Генераторная функция, которая возвращает транзакции с заданной валютой."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction
    # yield [transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] ==  code]


def transaction_descriptions(transactions: Any) -> Generator:
    """Генератор, который принимает список словарей
    с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")
        # yield [transaction.get("description") for transaction in transactions]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать
    номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:16]
    # yield [f"{num[0:4]} {num[4:8]} {num[8:12]} {num[-4:]}" for num in ("{:016d}".format(j) for j in range(start, stop +1))]
