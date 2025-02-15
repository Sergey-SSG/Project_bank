from src.masks import get_mask_account, get_mask_card_number

from src.widget import mask_account_card, get_date

from src.widgett import mask_account_card, get_date


if __name__ == "__main__":

    # Пример использования:
    print(get_mask_account(73654108430135874305))
    # выведет **4305

    # Пример использования:
    print(get_mask_card_number(7000792289606361))
    # Должно вывести: 7000 79** **** 6361

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
