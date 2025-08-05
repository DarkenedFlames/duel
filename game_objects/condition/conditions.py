
from game_objects.condition.base_condition import Condition

class Burning(Condition):
    def __init__(self): 
        self.name = "Burning"
        self.duration = 3
    def on_tick(self): self.target.recieve_damage(10)
    
class Freezing(Condition):
    def __init__(self): 
        self.name = "Freezing"
        self.duration = 2
    def on_apply(self): self.target.change_maximum_action(-20)
    def on_expire(self): self.target.change_maximum_action(20)
    
class Vulnerable(Condition):
    def __init__(self): 
        self.name = "Vulnerable"
        self.duration = 2
    def on_apply(self): self.target.change_armor(-20)
    def on_expire(self): self.target.change_armor(20)
    
    
    