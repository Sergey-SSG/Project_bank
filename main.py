from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":

    # Пример использования:
    print(get_mask_account(73654108430135874305))
    # выведет **4305

    # Пример использования:
    print(get_mask_card_number(7000792289606361))
    # Должно вывести: 7000 79** **** 6361
