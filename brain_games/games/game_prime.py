from random import randint


def is_prime(num: int) -> bool:
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def get_args() -> tuple:
    number = randint(2, 101)
    expression = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return expression, correct_answer


def get_rules() -> str:
    return "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."