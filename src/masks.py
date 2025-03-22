import logging

logging.basicConfig(
    filename="logs/masks.log",
    encoding="utf-8",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger("masks")


def get_mask_card_number(card: str) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
    номер разбит по блокам по 4 цифры, разделенным пробелами."""

    # Приводим card к строке
    card_str = str(card)
    # Длина номера карты (обычно 16)
    n = len(card_str)
    logger.debug(f"Получен номер: {n}")
    # Первые 6 и последние 4 цифры остаются видимыми
    visible_indices = set(range(6)) | set(range(n - 4, n))
    # Формируем новую строку с масками
    masked = "".join(ch if i in visible_indices else "*" for i, ch in enumerate(card_str))
    # Разбиваем на блоки по 4 символа
    groups = [masked[i : i + 4] for i in range(0, n, 4)]
    logger.info(f"Замаскированный номер карты: {groups}")
    return " ".join(groups)


def get_mask_account(account_number: str) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки."""
    account_str = str(account_number)
    logger.debug(f"Получен номер счета: {account_str}")
    last_four = account_str[-4:]
    logger.info(f"Замаскированный номер счета: {last_four}")
    return "**" + last_four


if __name__ == "__main__":

    # Пример использования:
    print(get_mask_card_number("7000792289606361"))
    # Должно вывести: 7000 79** **** 6361

    # Пример использования:
    print(get_mask_account("73654108430135874305"))
    # выведет **4305
