import json
import logging
import os

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# logging.basicConfig(
#     filename="logs/utils.log",
#     encoding="utf-8",
#     filemode="w",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
#
# logger = logging.getLogger("utils")


def load_transactions(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    if not os.path.exists(file_path):
        return []
    logger.info(f"Загрузка транзакций из файла: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно прочитан и содержит список транзакций.")
                return data
        except json.JSONDecodeError:
            logger.error(f"Файл {file_path} содержит некорректный JSON.")
            return []

    return []
