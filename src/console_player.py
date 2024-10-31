from hand import Hand
from player import Player


class ConsolePlayer(Player):

    def pick_action(
        self, player_hand: Hand, dealer_revealed_card: int
    ) -> Player.Actions:
        print("\nPlayer hand: ", player_hand)
        print("Dealer revealed card: ", dealer_revealed_card)
        while True:
            action = input("[H]it / [S]tand: ")
            match action[0].upper():
                case "H":
                    return Player.Actions.HIT
                case "S":
                    return Player.Actions.STAND
                case _:
                    print("Input is invalid")

    def notify_game_result(
        self, result: Player.GameResults, player_value: int, dealer_value: int
    ) -> None:
        print(f"\nYou have {player_value}, dealer has {dealer_value}")

        match result:
            case Player.GameResults.WIN:
                print("You win!")
            case Player.GameResults.LOSE:
                print("You lose!")
            case Player.GameResults.PUSH:
                print("Push!")
