from black import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card_account: str) -> str:
    """Функция mask_account_card принимает на вход название карты или счет
    и выводит название и номер карты"""
    pass

    return f"{get_mask_card_number(card)} {get_mask_account(account_number)}"


def get_date(date_str: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    # Для карты
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    # Для счета
    print(mask_account_card("Счет 73654108430135874305"))

    # Дата
    print(get_date("2024-03-11T02:26:18.671407"))
    # Должно вывести: "11.03.2024"
