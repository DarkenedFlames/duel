from handlers.event_handling import events, Events
from game_objects.item.endless_bag import bag
import time

class TurnHandler:
    def __init__(self, players):
        self.players = players
        self.current_index = 0
    
    def clear(self):
        print("\n" * 1000)
    
    @property
    def next_index(self):
        return (self.current_index + 1) % len(self.players)
    
    @property
    def current_player(self):
        return self.players[self.current_index]
        
    @property
    def next_player(self):
        return self.players[self.next_index]
    
    def next_turn(self):
        """Switch to the next player."""
        self.current_index = self.next_index

    def handle_turn(self):        
        player = self.current_player
        opponent = self.next_player
        
        self.clear()
        events.fire(Events.turn_start, player)
        player.current_action = player.maximum_action
        player.tick_conditions()
        item = bag.draw_item() 
        item.pickup(player)
        
        while player.current_action > 0:
            print(f"🔰 \n{player.name}'s Turn")
            print(f"⚔️ Action: {player.current_action} / {player.maximum_action}")
            print(f"❤️ Health: {player.current_health} / {player.maximum_health}")
            print(f"🛡️ Armor: {player.armor}")
            print(f"💠 Shield: {player.shield}")
            print("\n⛏️ Equipment")
            for slot, item in player.equipment.items():
                if not item:
                    print(f"▫️{slot}: Empty")
                else:
                    print(f"▫️{slot}: {item.name}")
                    
            print(f"\n🖤 {opponent.name}'s HP: {opponent.current_health} / {opponent.maximum_health}")
            print("\nChoose an action:")
            print("1. 🗡️ Attack")
            print("2. 🎒 Items")
            print("3. 🔚 End Turn")
            
            choice = input("🔘 ").strip()
            match choice:
                case "1": player.attack(opponent)
                case "2": self.item_menu()
                case "3": break
                case _:   print("↪️ Invalid choice, try again.")
        
        if opponent.current_health <= 0:
            return {"winner": player, "loser": opponent}
        if player.current_health <= 0:
            return {"winner": opponent, "loser": player}

        events.fire(Events.turn_end, player)
        return None
    
    def item_menu(self):
        player = self.current_player
        if not player.inventory:
            print("🫳 Your inventory is empty.")
            return
        
        print("\n🎒 Inventory:")
        for i, item in enumerate(player.inventory, start=1):
            print(f"{i}. {item.name}")
        print(f"{len(player.inventory)+1}. Back")
        
        try:
            choice = int(input("> ").strip())
            if choice == len(player.inventory) + 1:
                return
            chosen_item = player.inventory[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return
        
        print(f"\n📦 You selected {chosen_item.name}. What would you like to do?")
        print("1. 🗝️ Use")
        print("2. ⚒️ Equip")
        print("3. 🔙 Back")
        
        action = input("🔘 ").strip()
        if action == "1":
            chosen_item.use()
        elif action == "2":
            chosen_item.equip()
    
            
