import operator

from random import randint

signs = ("+", "-", "*")
commands = (operator.add, operator.sub, operator.mul)


def calculate(num1: int, num2: int, indx) -> str:
    function = commands[indx]
    result = function(num1, num2)
    return str(result)

def get_args() -> tuple:
    rules = "What is the result of the expression?"
    a = randint(1, 20)
    b = randint(1, 20)
    indx = randint(0, 3)
    expression = f"{a} {signs[indx]} {b}"
    currect_answer = calculate(a, b, indx)
    return (rules, expression, currect_answer)