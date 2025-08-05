from handlers.event_handling import Events, events

MESSAGES = {
    Events.game_start:      "Game on!",
    Events.game_end:        "Game over!",
    Events.turn_start:      "{source.name}'s turn has begun.",
    Events.turn_end:        "{source.name}'s turn has ended.",
    Events.item_pickup:     "{source.holder.name} has picked up {source.name}.",
    Events.item_destroy:    "{source.holder.name} has destroyed {source.name}.",
    Events.item_equip:      "{source.holder.name} has equipped {source.name}.",
    Events.item_unequip:    "{source.holder.name} has unequipped {source.name}.",
    Events.item_attack:     "{source.holder.name} has attacked {source.target.name} with {source.name}.",
    Events.condition_apply: "{source.name} has been applied to {source.target.name}.",
    Events.condition_expire:"{source.name} has expired on {source.target.name}.",
    Events.player_current_health_changed:          "{source.name}'s health has changed from {old} to {new}.",
    Events.player_maximum_health_changed:  "{source.name}'s maximum health has changed from {old} to {new}.",
    Events.player_current_action_changed:          "{source.name}'s action has changed from {old} to {new}.",
    Events.player_maximum_action_changed:  "{source.name}'s maximum action has changed from {old} to {new}.",
    Events.player_armor_changed:           "{source.name}'s armor has changed from {old} to {new}.",
    Events.player_death:                   "{source.name} has died!"
}

def register_messages():
    for event_name, template in MESSAGES.items():
        def make_listener(msg_template):
            def listener(source, **kwargs):
                print(msg_template.format(source=source, **kwargs))
            return listener
        events.register(event_name, make_listener(template))

register_messages()