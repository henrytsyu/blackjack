from hand import Hand
from player import Player


class ConsolePlayer(Player):

    def pick_action(
        self, player_hand: Hand, dealer_revealed_card: int
    ) -> Player.Actions:
        print("Player hand: ", player_hand)
        print("Dealer revealed card: ", dealer_revealed_card)
        while True:
            action = input("[H]it / [S]tand: ")
            match action:
                case "H":
                    return Player.Actions.HIT
                case "S":
                    return Player.Actions.STAND
                case _:
                    print("Input is invalid")

    def notify_game_result(self, result: Player.GameResults) -> None:
        print(result)
