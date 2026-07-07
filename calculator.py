def add(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.
    """
    # BUG: Should use +
    return a - b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
