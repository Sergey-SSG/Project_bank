import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_URL = "https://api.apilayer.com/exchangerates_data"
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount, currency: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли."""
    if currency == "RUB":
        return float(amount)

    response = requests.get(f"{API_URL}/latest?base={currency}&symbols=RUB", headers={"apikey": API_KEY})

    if response.status_code != 200:
        raise Exception("Error fetching exchange rates")

    rates = response.json()
    return float(amount) * rates["rates"]["RUB"]
