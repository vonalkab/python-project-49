from brain_games.game_engine import play_game
from brain_games.games.game_gcd import get_args, get_rules


def main() -> None:
    play_game(get_rules, get_args)


if __name__ == "__main__":
    main()