from functools import wraps


def log(filename=None):
    """Декоратор для логирования начала и конца выполнения функции."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Логируем начало выполнения функции
                log_message = f"Starting {func.__name__}\n"

                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                result = func(*args, **kwargs)

                # Логируем успешное завершение функции
                log_message = f"{func.__name__} ok\n"

                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                return result
            except Exception as e:
                # Логируем ошибку
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                raise  # Повторно выбрасываем исключение после логирования

        return wrapper

    return decorator
