from hand import Hand
from shoe import Shoe


class Dealer:

    MIN_STAND = 17

    def __init__(self, shoe: Shoe):
        self.hand = Hand()
        self.shoe = shoe
        self.revealed_card = shoe.deal()
        self.hand.add(self.revealed_card)

    def reset(self) -> None:
        self.hand = Hand()
        self.revealed_card = self.shoe.deal()
        self.hand.add(self.revealed_card)

    def draw_until_min_stand(self) -> None:
        while self.hand.evaluate() < Dealer.MIN_STAND:
            self.hand.add(self.shoe.deal())

    def evaluate(self) -> int:
        return self.hand.evaluate()
