import pytest

from src.decorators import log


# Тесты
@log()
def successful_function(x, y):
    return x + y


@log()
def error_function(x, y):
    return x / 0  # Искусственно вызываем ошибку деления на ноль


def test_successful_function(capsys):
    result = successful_function(1, 2)

    # Проверяем результат выполнения функции
    assert result == 3

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "Starting successful_function" in captured.out
    assert "successful_function ok" in captured.out


# def test_error_function(capsys):
#     with pytest.raises(ZeroDivisionError):
#         error_function(1, 0)
#
#     # Проверяем вывод в консоль на наличие ошибки
#     captured = capsys.readouterr()
#     assert "Starting error_function" in captured.out
#     assert "error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.err


def test_file_logging(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def another_successful_function(a, b):
        return a * b

    another_successful_function(3, 4)

    # Проверяем содержимое файла логов
    with open(log_file) as f:
        logs = f.read()

    assert "Starting another_successful_function" in logs
    assert "another_successful_function ok" in logs
