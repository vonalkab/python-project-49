import prompt


def play_game(name: str, rules: str, expression: str, correct_answer: str) -> None:
    print(rules)
    counter = 0
    while counter < 3:
        user_answer = prompt.string(f"Question: {expression}\nYour answer: ")
        if user_answer == correct_answer:
            counter += 1
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")