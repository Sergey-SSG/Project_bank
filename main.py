import logging
import json
import pandas as pd
import csv

from src.transactions import find_transactions_by_description, count_transaction_categories
from src.csv_xlsx_file import read_csv_file, read_xlsx_file
from src.decorators import log
from src.external_api import convert_to_rub
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
# from src.widget import get_date, mask_account_card
from src.widget_variant_2 import get_date, mask_account_card

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/main.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# logging.basicConfig(
#     filename='logs/main.log', encoding='utf-8',
#     filemode='w',
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
#
# logger = logging.getLogger('main')

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        with open("data/operations.json", 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        print(type(transactions))
        file_type = 'JSON'

    elif choice == '2':
        with open("src/transactions.csv", 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = list(reader)
        print(type(transactions))
        file_type = 'CSV'

    elif choice == '3':
        transactions = pd.read_excel("src/transactions_excel.xlsx").to_dict(orient='records')
        print(type(transactions))
        file_type = 'XLSX'
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    print(f"Для обработки выбран {file_type}-файл.")

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ")
        statuses = ['EXECUTED', 'CANCELED', 'PENDING']
        if status.upper() in statuses:
            break
        print(f"Статус операции \"{status}\" недоступен.")

    status = status.upper()  # приведение к верхнему регистру
    filtered_transactions = [tx for tx in transactions if tx.get('state', '').upper() == status]

    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ")
    if sort_choice.lower() == 'да':
        order_choice = input("Сортировать по возрастанию или по убыванию?\nПользователь: ")
        if order_choice.lower() == "по убыванию":
            filtered_transactions.sort(key=lambda x: x['date'], reverse=True)
        else:
            filtered_transactions.sort(key=lambda x: x['date'])

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
    if currency_choice.lower() == 'да':
        filtered_transactions = [tx for tx in filtered_transactions if tx['currency'] == 'RUB']

    keyword_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
    if keyword_choice.lower() == 'да':
        keyword = input("Введите слово для фильтрации: ")
        filtered_transactions = find_transactions_by_description(filtered_transactions, keyword)


    print("Распечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for tx in filtered_transactions:
        print(f"{tx['date']} {tx['description']}")
        print(f"Счет **{tx['account'][-4:]}")
        print(f"Сумма: {tx['amount']} {tx['currency']}\n")

if __name__ == "__main__":
    main()

    # # Пример использования:
    # print(get_mask_account("73654108430135874305"))
    # # выведет **4305
    #
    # # Пример использования:
    # print(get_mask_card_number("7000792289606361"))
    # # Должно вывести: 7000 79** **** 6361
    #
    # # Пример использования:
    # cards_nums = [
    #     "Maestro 1596837868705199",
    #     "Счет 64686473678894779589",
    #     "MasterCard 7158300734726758",
    #     "Счет 35383033474447895560",
    #     "Visa Classic 6831982476737658",
    #     "Visa Platinum 8990922113665229",
    #     "Visa Gold 5999414228426353",
    #     "Счет 73654108430135874305",
    # ]
    # for cards in cards_nums:
    #     print(mask_account_card(cards))
    #
    #     # Дата
    #     print(get_date("2024-03-11T02:26:18.671407"))
    #     # Должно вывести: "11.03.2024"
    #
    # # Пример использования:
    # data = [
    #     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    # ]
    #
    # print(filter_by_state(data))
    # print(sort_by_date(data))
    #
    # # Пример использования:
    # transactions = [
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод организации",
    #         "from": "Счет 75106830613657916952",
    #         "to": "Счет 11776614605963066702",
    #     },
    #     {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188",
    #     },
    #     {
    #         "id": 873106923,
    #         "state": "EXECUTED",
    #         "date": "2019-03-23T01:09:46.296404",
    #         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 44812258784861134719",
    #         "to": "Счет 74489636417521191160",
    #     },
    #     {
    #         "id": 895315941,
    #         "state": "EXECUTED",
    #         "date": "2018-08-19T04:27:37.904916",
    #         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод с карты на карту",
    #         "from": "Visa Classic 6831982476737658",
    #         "to": "Visa Platinum 8990922113665229",
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод организации",
    #         "from": "Visa Platinum 1246377376343588",
    #         "to": "Счет 14211924144426031657",
    #     },
    # ]
    #
    # print('\nFiltered "USD": ')
    # usd_transactions = filter_by_currency(transactions, "USD")
    # for _ in range(2):
    #     print(next(usd_transactions))
    #
    # print("\nTransaction: ")
    # descriptions = transaction_descriptions(transactions)
    # for _ in range(5):
    #     print(next(descriptions))
    #
    # print("\nCard_numbers: ")
    # for card_number in card_number_generator(1, 5):
    #     print(card_number)
    #
    #
    # # Пример использования:
    # @log(filename="mylog.txt")
    # def my_function(x, y):
    #     return x + y
    #
    #
    # print("\nMy_sum:")
    # print(my_function(1, 2))
    #
    # # Пример использования:
    # # Перестал работать бесплатный API
    print("\nconvert_eur_rub:", convert_to_rub("100", "EUR"), "rub.")
    print("\nconvert_usd_rub:", convert_to_rub("100", "USD"), "rub.")
    #
    # # Пример использования:
    # # print("\nload_transactions:", load_transactions("data/operations.json"))
    # transactions = load_transactions("data/operations.json")
    # if transactions:
    #     logger.info(f"Загружено {len(transactions)} транзакций.")
    #     # print(f"\nLoaded {len(transactions)} transactions.")
    # else:
    #     # print("No transactions loaded.")
    #     logger.warning("Транзакции не были загружены.")
    # file_type = 'JSON'
    #
    # # Пример использования:
    # csv_file_path = "src/transactions.csv"
    # xlsx_file_path = "src/transactions_excel.xlsx"
    # print("\n")
    # # Чтение данных из CSV
    # csv_data = read_csv_file(csv_file_path)
    # if csv_data is not None:
    #     print(csv_data)
    # print("\n")
    # # Чтение данных из XLSX
    # xlsx_data = read_xlsx_file(xlsx_file_path)
    # if xlsx_data is not None:
    #     print(xlsx_data)
