from hand import Hand


class DealerHand(Hand):

    MIN_STAND = 17

    def __init__(self, card1: int, card2: int):
        Hand.__init__(self, card1, card2)

    def revealed_card(self) -> int:
        return self.cards()[0]

    def reached_min_stand(self) -> bool:
        return sum(self.cards()) >= DealerHand.MIN_STAND
