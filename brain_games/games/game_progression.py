from random import randint, randrange


def get_progression() -> list:
    length = randint(5, 10)
    begining = randint(1, 20)
    step = randint(1, 5)
    progression = [str(begining)]
    for i in range(1, length):
        new_element = int(progression[i - 1]) + step
        progression.append(str(new_element))
    return progression


def get_args() -> tuple:
    progression = get_progression()
    indx = randrange(len(progression))
    correct_answer = progression[indx]
    progression[indx] = ".."
    expression = " ".join(progression)
    return expression, correct_answer


def get_rules() -> str:
    return "What number is missing in the progression?"