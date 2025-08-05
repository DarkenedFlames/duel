from handlers.event_handling import events, Events
from handlers.turn_handling import TurnHandler
from handlers import messages
from game_objects.player import Player

class Game:
    def __init__(self):
        self.players = [Player("Hero"), Player("Villain")]
        self.turns = TurnHandler(self.players)
    
    def run(self):
        events.fire(Events.game_start, self)

        while True:
            result = self.turns.handle_turn()
            if result:
                self.end_game(**result)
                break
            self.turns.next_turn()

    def end_game(self, winner, loser):
        loser.die()
        print(f"{winner.name} wins!")
        events.fire(Events.game_end, self)
        
        