from random import randint


def is_even(number: int) -> bool:
    return "yes" if number % 2 == 0 else "no"


def get_args() -> tuple:
    rules = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    number = randint(1, 1000)
    expression = number
    currect_answer = is_even(number)
    return (rules, expression, currect_answer)