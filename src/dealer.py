from dealer_hand import DealerHand
from hand import Hand
from player import Player
from shoe import Shoe


class Dealer:

    MIN_STAND = 17

    def __init__(self, player: Player):
        self.__player = player
        self.__shoe = Shoe()

    def run_game(self) -> None:
        player_hand = Hand(self.__shoe.deal(), self.__shoe.deal())
        dealer_hand = DealerHand(self.__shoe.deal(), self.__shoe.deal())

        player_is_stand = False
        while not player_is_stand and not player_hand.busted():
            player_action = self.__player.pick_action(
                player_hand, dealer_hand.revealed_card()
            )
            match player_action:
                case Player.Actions.HIT:
                    player_hand.add(self.__shoe.deal())
                case Player.Actions.STAND:
                    player_is_stand = True

        if not player_hand.busted():
            self.__dealer_draw_until_min_stand(dealer_hand)
        self.__player.notify_game_result(Dealer.__game_result(player_hand, dealer_hand))

    def __dealer_draw_until_min_stand(self, dealer_hand: DealerHand) -> None:
        # Draw until hard 17
        while not dealer_hand.reached_min_stand():
            dealer_hand.add(self.__shoe.deal())

    def __game_result(player_hand: Hand, dealer_hand: DealerHand) -> Player.GameResults:
        if player_hand < dealer_hand:
            return Player.GameResults.LOSE
        if player_hand == dealer_hand:
            return Player.GameResults.PUSH
        return Player.GameResults.WIN
