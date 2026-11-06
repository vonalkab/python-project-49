from random import randint


def get_args() -> tuple:
    common_devisor = randint(1, 30)
    factor1 = randint(1, 10)
    factor2 = randint(1, 10)
    num1 = factor1 * common_devisor
    num2 = factor2 * common_devisor
    expression = f"{num1} {num2}"
    correct_answer = str(get_gcd(num1, num2))
    return expression, correct_answer


def get_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    gcd = a
    return gcd


def get_rules() -> str:
    return "Find the greatest common divisor of given numbers."