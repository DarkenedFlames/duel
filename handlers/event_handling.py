class EventHandler:
    def __init__(self):
        self.listeners = {}
    
    def register(self, event, listener):
        self.listeners.setdefault(event, []).append(listener)
    
    def fire(self, event, source, **kwargs):
        kwargs["_event_name"] = event  # Pass event name to listeners
        for listener in self.listeners.get(event, []):
            listener(source, **kwargs)


events = EventHandler()


class Events:
    game_start = "game_start"
    game_end = "game_end"
    
    turn_start = "turn_start"
    turn_end = "turn_end"
    
    condition_apply = "condition_apply"
    condition_expire = "condition_expire"
    
    item_pickup = "item_pickup"
    item_destroy = "item_destroy"
    item_use = "item_use"
    item_equip = "item_equip"
    item_unequip = "item_unequip"
    item_attack = "item_attack"
    
    player_current_health_changed = "player_current_health_changed"
    player_maximum_health_changed = "player_maximum_health_changed"
    player_current_action_changed = "player_current_action_changed"
    player_maximum_action_changed = "player_maximum_action_changed"
    player_armor_changed = "player_armor_changed"
    player_shield_changed = "player_shield_changed"
    player_death = "player_death"