#Robert Frasier

# Display game title and instructions
def show_instructions():
    print("\nThrone of Bone - A Dark Fantasy Adventure")
    print("Goal: Collect 8 relics of light to defeat the Lich King.")
    print("Commands:")
    print(" go [North|South|East|West]")
    print(" get [item name]\n")

# Display the current room, inventory, and item (if any)
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room}.")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("_" * 40)

# Dictionary that defines the game map
# Each room contains possible directions to other rooms
# Some rooms also contain an item the player can collect
rooms = {
    'Graveborn Gate': {
        'North': 'Sunken Courtyard'
        # No item here — this is the starting room
    },
    'Sunken Courtyard': {
        'North': 'Hall of whispers',
        'South': 'Sunken Courtyard',
        'East': 'Chapel of Lost Saints',
        'West': 'Crypt of the Damned',
        'item': 'Bloodroot Flower'
    },
    'Crypt of the Damned': {
        'East': 'Sunken Courtyard',
        'item': 'Soulfire Urn'
    },
    'Chapel of Lost Saints': {
        'North': 'Frozen Garden',
        'West': 'Sunken Courtyard',
        'item': 'Sanctified Candle'
    },
    'Hall of whispers': {
        'North': 'Throne of Bone',
        'South': 'Sunken Courtyard',
        'West': 'Cursed Library',
        'item': 'Whisperstone Pendant'
    },
    'Cursed Library': {
        'North': 'Ruined Armory',
        'East': 'Hall of whispers',
        'item': 'Pages of Binding'
    },
    'Ruined Armory': {
        'South': 'Cursed Library',
        'East': 'Moonlit Watchtower',
        'item': 'Shattered Shield'
    },
    'Moonlit Watchtower': {
        'West': 'Ruined Armory',
        'item': "Watcher's Eye"
    },
    'Frozen Garden': {
        'South': 'Chapel of Lost Saints',
        'item': 'Frozen Lily'
    },
    'Throne of Bone': {
        # No item here — this is the final boss room
    }
}


def main():
    # Player starting location
    current_room = 'Graveborn Gate'

    # Initialize empty inventory
    inventory = []

    # Display game instructions
    show_instructions()

    # Begin gameplay loop
    while True:
        # Show player status at the beginning of each turn
        show_status(current_room, inventory, rooms)

        # Get player's next move as input
        move = input("Enter your move: ").strip()

        # Handle movement commands
        if move.lower().startswith('go '):
            direction = move[3:].capitalize()

            # Check if the direction is valid from the current room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Check for win/lose condition upon entering the villain's room
                if current_room == 'Throne of Bone':
                    if len(inventory) == 8:
                        print("\nYou confront Varnor, the Lich King, with all 8 relics!")
                        print("His power fades... You are victorious!")
                        print("Thanks for playing. You win!")
                    else:
                        print("\nYou enter the Throne of Bone unprepared.")
                        print("Varnor devours your soul. NOM NOM...GAME OVER!")
                        print("Restart the game to try again.")
                    break
            else:
                print("You can't go that way.")

        # Handle item collection
        elif move.lower().startswith('get '):
            item_name = move[4:]
            room = rooms[current_room]

            # Check if the current room has the item and the name matches
            if 'item' in room and room['item'].lower() == item_name.lower():
                if item_name not in inventory:
                    inventory.append(item_name)
                    print(f"{item_name} has been added to your inventory.")
                    del room['item']  # Remove the item from the room
                else:
                    print("You already have that item.")
            else:
                print("No such item in this room.")

        # Handle invalid input
        else:
            print("Invalid command. Try 'go [direction]' or 'get [item]'.")

# Run the game
if __name__ == "__main__":
    main()
