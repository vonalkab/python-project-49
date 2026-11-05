from brain_games.game_engine import play_game
from brain_games.games.game_even import get_args


def main() -> None:
    play_game(get_args)


if __name__ == "__main__":
    main()