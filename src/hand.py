class Hand:

    ACE_CARD = 1
    ACE_BONUS = 10
    MAX_VALUE = 21
    BLACKJACK_HAND = [1, 10]

    def __init__(self):
        self.value = 0
        self.has_usable_ace = False

    def add(self, card: int) -> None:
        self.value += card
        self.has_usable_ace = self.value <= Hand.MAX_VALUE - Hand.ACE_BONUS and (
            self.has_usable_ace or card == Hand.ACE_CARD
        )

    def evaluate(self) -> int:
        if self.busted():
            return -1
        return self.value + (Hand.ACE_BONUS if self.has_usable_ace else 0)

    def busted(self) -> bool:
        return self.value > Hand.MAX_VALUE

    def is_blackjack(self) -> bool:
        return sorted(self.cards) == Hand.BLACKJACK_HAND
