import prompt

from brain_games.cli import welcome_user


def play_game(func) -> None:
    name = welcome_user()
    for _ in range(3):
        rules, expression, correct_answer = func()
        print(rules)
        user_answer = prompt.string(f"Question: {expression}\nYour answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")