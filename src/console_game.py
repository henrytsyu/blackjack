from console_player import ConsolePlayer
from dealer import Dealer


def main() -> None:
    player = ConsolePlayer()
    dealer = Dealer(player)
    dealer.run_game()


if __name__ == "__main__":
    main()
