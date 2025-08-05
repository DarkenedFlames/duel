
from handlers.event_handling import Events, events

class Item:
    def __init__(self):
        self.name           = None
        self.holder         = None
        self.equipment      = None
        self.inventory      = None
        self.equipment_type = None
        self.target         = None

    def pickup(self, holder):
        self.holder    = holder
        self.equipment = holder.equipment
        self.inventory = holder.inventory
        self.inventory.append(self)
        self.on_pickup()
        events.fire(event=Events.item_pickup, source=self)

    def use(self):
        self.on_use()
        events.fire(event=Events.item_use, source=self)

    def equip(self):
        to_replace = self.equipment[self.equipment_type]
        if to_replace:
            to_replace.unequip()
        if self in self.inventory:
            self.inventory.remove(self)
        
        self.equipment[self.equipment_type] = self
        self.on_equip()
        events.fire(event=Events.item_equip, source=self)

    def unequip(self):        
        if (
            self.equipment_type in self.equipment
            and 
            self.equipment[self.equipment_type] is self
        ):
            self.equipment[self.equipment_type] = None
            self.inventory.append(self)
            self.on_unequip()
            events.fire(event=Events.item_unequip, source=self)

    def destroy(self):
        """Remove item completely from inventory and equipment."""
        if self in self.inventory:
            self.inventory.remove(self)
        for slot, item in self.equipment.items():
            if item is self:
                self.equipment[slot] = None
        self.on_destroy()
        events.fire(event=Events.item_destroy, source=self)

    def attack(self, target):
        self.target = target
        self.on_attack()
        events.fire(event=Events.item_attack, source=self)

    def on_pickup(self): pass
    def on_use(self): pass
    def on_equip(self): pass
    def on_unequip(self): pass
    def on_destroy(self): pass
    def on_attack(self): pass
    
    def __hash__(self): return hash(self.__class__.__name__)
    def __eq__(self, other): return isinstance(other, self.__class__)
    