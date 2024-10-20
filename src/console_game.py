from game import Game


class ConsoleGame(Game):
    
    def player_actions(self) -> None:
        player_stand = False
        while not self.player.busted() and not player_stand:
            action = input("[H]it / [S]tand: ")
            match action:
                case "H":
                    self.player.hit()
                case "S":
                    player_stand = True
                case _:
                    print("Input is invalid")

    def dealer_actions(self) -> None:
        if self.player.busted():
            return
        self.dealer.draw_until_min_stand()
