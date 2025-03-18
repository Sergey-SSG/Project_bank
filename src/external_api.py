import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_URL = "https://api.apilayer.com/exchangerates_data"
headers = {"apikey": os.getenv("API_KEY")}


def convert_to_rub(amount, currency: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли."""
    if currency == "RUB":
        return float(amount)

    if currency in ["USD", "EUR"]:

        response = requests.get(f"{API_URL}/convert?from={currency}&to=RUB&amount={amount}", headers=headers)

        response.raise_for_status()
        conversion_data = response.json()
        return float(conversion_data["result"])

    return float(amount)
