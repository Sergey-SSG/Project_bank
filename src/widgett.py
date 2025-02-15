import re

from black import datetime


def mask_account_card(text):
    # Ищем последовательность цифр в конце строки
    match = re.search(r"(\d+)$", text)
    if not match:
        return text  # если цифр нет, возвращаем исходную строку

    number = match.group(1)
    prefix = text[: match.start(1)].rstrip()

    # Если это информация о счете (начинается со слова "Счет")
    if prefix.startswith("Счет"):
        # Для счета маскируем всё, кроме последних 4 цифр,
        # добавляя две звёздочки перед ними.
        masked_num = "**" + number[-4:]
        return f"{prefix} {masked_num}"
    else:
        # Предполагаем, что это карта
        # Для карты оставляем первые 6 и последние 4 цифры видимыми, остальное заменяем на "*"
        if len(number) <= 10:
            # Если число короче обычного номера карты – просто возвращаем его без маскировки
            return f"{prefix} {number}"

        visible_start = number[:6]
        visible_end = number[-4:]
        num_mask = "*" * (len(number) - 10)
        masked_num = visible_start + num_mask + visible_end
        return f"{prefix} {masked_num}"


def get_date(date_str: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


# Примеры использования:
if __name__ == "__main__":
    # Для карты
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    # Для счета
    print(mask_account_card("Счет 73654108430135874305"))

    # Дата
    print(get_date("2024-03-11T02:26:18.671407"))
    # Должно вывести: "11.03.2024"
