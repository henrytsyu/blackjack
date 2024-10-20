from hand import Hand
from shoe import Shoe


class Player:

    def __init__(self, shoe: Shoe):
        self.hand = Hand()
        self.shoe = shoe
        self.reset()

    def reset(self) -> None:
        self.hand = Hand()
        # Players are dealt 2 cards at the start of each game
        self.hit()
        self.hit()

    def hit(self) -> None:
        self.hand.add(self.shoe.deal())

    def busted(self) -> bool:
        return self.hand.busted()

    def evaluate(self) -> int:
        return self.hand.evaluate()
