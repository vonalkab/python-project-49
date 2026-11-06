from random import randint


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_args() -> tuple:
    number = randint(1, 1000)
    expression = number
    correct_answer = "yes" if is_even(number) else "no"
    return (expression, correct_answer)


def get_rules() -> str:
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."
