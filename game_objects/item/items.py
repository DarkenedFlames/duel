
from game_objects.item.base_item import Item
from game_objects.condition.conditions import Burning

class HealingPotion(Item):
    def __init__(self): 
        self.name = "Healing Potion"
        self.equipment_type = "Potion"
    def on_use(self): 
        self.holder.receive_healing(20)
        self.holder.change_current_action(-50)

class SwordOfFlames(Item):
    def __init__(self):
        self.name = "Sword of Flames"
        self.equipment_type = "Weapon"

    def on_attack(self):
        burning = Burning()
        burning.apply(self.target)
        self.target.recieve_damage(20, "physical")
        self.holder.change_current_action(-50)
        


