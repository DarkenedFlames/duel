
from handlers.event_handling import Events, events
# ==============================
# Condition
# ==============================
class Condition:
    def __init__(self):
        self.duration = None
        self.target = None

    def apply(self, target):
        if self not in target.conditions:
            self.target = target
            target.conditions.add(self)
            self.on_apply()
            events.fire(
                event=Events.condition_apply, 
                source=self
            )
    
    def tick(self):
        self.on_tick()
        self.duration -= 1
        if self.duration <= 0:
            self.expire()

    def expire(self):
        self.target.conditions.remove(self)
        self.on_expire()
        events.fire(
            event=Events.condition_expire,
            source=self   
        )
    
    def on_apply(self): pass
    def on_tick(self): pass
    def on_expire(self): pass
    
    def __hash__(self): return hash(self.__class__.__name__)
    def __eq__(self, other): return isinstance(other, self.__class__)