from brain_games.cli import welcome_user
from brain_games.games.game_even import play_game


def main() -> None:
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()