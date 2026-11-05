from random import randint


def is_even(number: int) -> bool:
    return "yes" if number % 2 == 0 else "no"


def get_args() -> tuple:
    number = randint(1, 1000)
    expression = number
    correct_answer = is_even(number)
    return (expression, correct_answer)


def get_rules() -> str:
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."