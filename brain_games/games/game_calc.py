import operator
from random import randint

signs = ("+", "-", "*")
commands = (operator.add, operator.sub, operator.mul)


def calculate(num1: int, num2: int, indx: int) -> str:
    function = commands[indx]
    result = function(num1, num2)
    return str(result)


def get_args() -> tuple:
    a = randint(1, 20)
    b = randint(1, 20)
    indx = randint(0, 2)
    expression = f"{a} {signs[indx]} {b}"
    correct_answer = calculate(a, b, indx)
    return (expression, correct_answer)


def get_rules() -> str:
    return "What is the result of the expression?"
