from black import datetime, replace

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card_account: str) -> str:
    """Функция mask_account_card принимает на вход название карты или счет
    и выводит название и номер карты"""
    if "Счет" in name_card_account:
        number = int(name_card_account.replace("Счет", "").strip())
        return "Счет " + get_mask_account(number)
    else:  # Maestro 7000792289606361"
        numbers = get_mask_card_number(name_card_account[-16:])
        update_cart = " ".join(name_card_account.split()[:-1]) + " " + numbers
        return update_cart


def get_date(date_str: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    cards_nums = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    for cards in cards_nums:
        print(mask_account_card(cards))

    # Дата
    print(get_date("2024-03-11T02:26:18.671407"))
    # Должно вывести: "11.03.2024"
