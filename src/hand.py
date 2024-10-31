from functools import total_ordering
from typing import Self


@total_ordering
class Hand:

    ACE_CARD = 1
    ACE_BONUS = 10
    MAX_VALUE = 21
    BLACKJACK_HAND_SORTED = [1, 10]

    def __init__(self, card1: int, card2: int):
        self.__cards = [card1, card2]

    def cards(self) -> list[int]:
        return self.__cards

    def add(self, card: int) -> None:
        assert not self.busted()
        self.__cards.append(card)

    def evaluate(self) -> int:
        return sum(self.__cards) + (Hand.ACE_BONUS if self.has_usable_ace() else 0)

    def has_usable_ace(self) -> bool:
        return (
            Hand.ACE_CARD in self.__cards
            and sum(self.__cards) + Hand.ACE_BONUS <= Hand.MAX_VALUE
        )

    def busted(self) -> bool:
        return self.evaluate() > Hand.MAX_VALUE

    def is_blackjack(self) -> bool:
        return sorted(self.__cards) == Hand.BLACKJACK_HAND_SORTED

    def __str__(self) -> str:
        return str(self.__cards)

    def __lt__(self, other: Self) -> bool:
        return (
            self.busted() > other.busted()
            or (
                self.busted() == other.busted()
                and self.is_blackjack() < other.is_blackjack()
            )
            or (
                self.busted() == other.busted()
                and self.is_blackjack() == other.is_blackjack()
                and self.evaluate() < other.evaluate()
            )
        )

    def __eq__(self, other: Self) -> bool:
        return (
            self.busted() == other.busted()
            and self.is_blackjack() == other.is_blackjack()
            and self.evaluate() == other.evaluate()
        )
