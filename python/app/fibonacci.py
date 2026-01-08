from app.logging import logger


def fibonacci(n: int):
    """Return the first `n` Fibonacci numbers."""

    logger.debug(f"Received request to print {n} numbers from fibonacci sequence.")

    if n <= 0:
        return []

    fib = [0, 1]
    for _ in range(2, n):
        fib.append(sum(fib[-2:]))

    return fib[:n]
