from abc import ABC, abstractmethod
from dealer import Dealer
from player import Player
from shoe import Shoe


class Game(ABC):

    def __init__(self):
        self.shoe = Shoe()
        self.dealer = Dealer(self.shoe)
        self.player = Player(self.shoe)

    def run(self) -> None:
        self.player_actions()
        self.dealer_actions()

    @abstractmethod
    def player_actions(self) -> None:
        pass

    @abstractmethod
    def dealer_actions(self) -> None:
        pass
