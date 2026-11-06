import prompt

from brain_games.cli import welcome_user


def play_game(show_rules, get_game_args) -> None:
    name = welcome_user()
    print(show_rules())
    for _ in range(3):
        expression, correct_answer = get_game_args()
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