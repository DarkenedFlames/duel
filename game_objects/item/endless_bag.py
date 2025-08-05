
import random
from .items import SwordOfFlames, HealingPotion

POOL = [
    (SwordOfFlames, 1),
    (HealingPotion, 9)
    ]
    
    
# ==============================
# Endless Bag (Item Pool)
# ==============================
class EndlessBag:
    def __init__(self):
        self.item_pool = POOL
    
    def draw_item(self):
        items, weights    = zip(*self.item_pool)
        chosen_item_class = random.choices(items, weights=weights, k=1)[0]
        return chosen_item_class()
        
bag = EndlessBag()
        
        