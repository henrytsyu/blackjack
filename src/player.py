from abc import ABC, abstractmethod
from enum import Enum
from hand import Hand


class Player(ABC):

    Actions = Enum("Actions", ["HIT", "STAND"])
    GameResults = Enum("GameResults", ["WIN", "LOSE", "PUSH"])

    @abstractmethod
    def pick_action(self, player_hand: Hand, dealer_revealed_card: int) -> Actions:
        pass

    @abstractmethod
    def notify_game_result(self, result: GameResults) -> None:
        pass
