
import math
from handlers.event_handling import Events, events

# ==============================
# Player
# ==============================
class Player:
    def __init__(self, name):
        self.name = name
        self.conditions = set()
        self.inventory = []
        
        self.maximum_health = 100
        self.current_health = 100
        self.maximum_action = 100
        self.current_action = 100
        self.armor = 100
        self.shield = 100
        
        self.equipment = {
            "Head": None,
            "Torso": None,
            "Legs": None,
            "Accessory": None,
            "Weapon": None
        }
    
    @property
    def physical_modifier(self):
        return 100 / (100 + self.armor)
        
    @property
    def magical_modifier(self):
        return 100 / (100 + self.shield)
    
    def attack(self, other):
        weapon = self.equipment["Weapon"]
        if weapon:
            weapon.attack(other)
    
    def change_current_health(self, delta):
        old = self.current_health
        self.current_health = int(max(0, min(
            self.maximum_health, 
            self.current_health + delta
        )))
        new = self.current_health
        
        events.fire(
            event=Events.player_current_health_changed, 
            source=self,
            old=old, 
            new=new
        )
        
    def change_current_action(self, delta):
        old = self.current_action
        self.current_action = int(max(0, min(
            self.maximum_action, 
            self.current_action + delta
        )))
        new = self.current_action
        
        events.fire(
            event=Events.player_current_action_changed, 
            source=self,
            old=old, 
            new=new
        )
        
    def change_maximum_health(self, delta):
        old = self.maximum_health
        self.maximum_health = int(max(
            self.maximum_health + delta, 
            1
        ))
        new = self.maximum_health
        
        events.fire(
            event=Events.player_maximum_health_changed, 
            source=self,
            old=old, 
            new=new
        )
        
    def change_maximum_action(self, delta):
        old = self.maximum_action
        self.maximum_action = int(max(
            self.maximum_action + delta, 
            1
        ))
        new = self.maximum_action
        
        events.fire(
            event=Events.player_maximum_action_changed, 
            source=self,
            old=old, 
            new=new
        )
    
    def change_armor(self, delta):
        old = self.armor
        self.armor += delta
        new = self.armor
        
        events.fire(
            event=Events.player_armor_changed, 
            source=self,
            old=old, 
            new=new
        )
        
    def change_shield(self, delta):
        old = self.shield
        self.shield += delta
        new = self.shield
        
        events.fire(
            event=Events.player_shield_changed, 
            source=self,
            old=old, 
            new=new
        )
    
    def die(self):
        events.fire(event=Events.player_death, source=self)

    def recieve_damage(self, damage, damage_type="physical"):
        damage = max(damage, 0)
        modifier = getattr(
            self,
            f'{damage_type}_modifier',
            self.physical_modifier
        )
        self.change_current_health(-damage * modifier)
        
    def receive_healing(self, healing):
        healing = max(healing, 0)
        self.change_current_health(healing)

    def tick_conditions(self):
        for condition in self.conditions.copy():
            condition.tick()
