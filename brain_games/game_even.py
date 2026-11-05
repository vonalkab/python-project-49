from random import randint
import prompt


def is_even(number: int) -> bool:
    return number % 2 == 0


def play_game(name: str) -> None:
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    counter = 0
    while counter < 3:
        num = randint(1, 1000)
        user_answer = prompt.string(f"Question: {num}\nYour answer: ")
        correct_answer = "yes" if is_even(num) else "no"
        if user_answer.lower() == correct_answer:
            counter += 1
            print("Correct!")
        else:
            counter = 0
            print(f"\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")