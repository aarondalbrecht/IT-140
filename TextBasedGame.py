#Aaron Albrecht

def introduction():
    print("\nWelcome to Vampire Hunt")
    print("Your objective to collect all 6 items in the castle to defeat the vampire.")
    print("If you find the vampire before collecting all the items, it's game over.")

def instructions():
    print("\nYou can move between rooms by typing 'North', 'South', 'East', 'West'.")
    print("You can pickup an item by typing 'Pickup'.")
    print("Type 'Exit' to quit the game.")

def status(room, name, inventory):
    print(f"\nYou are currently in the {name}")
    print(f"Your inventory includes: {inventory}." if len(inventory) > 0 else "Your inventory is empty.")
    for key, value in room.items():
        if 'Item' not in room.keys():
            print(f"To the {key} is the {value}")
        elif key == 'Item':
              if value == 'Garlic' or value == 'Holy Water' or value == 'Armor':
                  print(f"You see some {value}")
              else:
                  print(f"You see a {value}")
        else:
            print(f"To the {key} is the {value}")


def main():
    introduction()
    instructions()
    #rooms, available directions, and item locations
    rooms = {
            'Kitchen': {'East': 'Dining Hall', 'Item': 'Garlic'},
            'Dining Hall': {'West': 'Kitchen', 'East': 'Ballroom', 'South': 'Vestibule', 'Item': 'Silver Sword'},
            'Ballroom': {'West': 'Dining Hall', 'South': 'Library', 'Item': 'Vampire'}, #Villian
            'Bathroom': {'East': 'Bedroom', 'Item': 'Holy Water'},
            'Bedroom': {'West': 'Bathroom', 'East': 'Vestibule', 'Item': 'Armor'},
            'Vestibule': {'West': 'Bedroom', 'East': 'Library', 'North': 'Dining Hall', 'South': 'Basement'},
            'Library': {'West': 'Vestibule', 'North': 'Ballroom', 'Item': 'Cross'},
            'Basement': {'North': 'Vestibule', 'Item': 'Crossbow'}
            }

    #initializing game state
    current_room_name = 'Vestibule'
    current_room = rooms['Vestibule']
    inventory = []

    #game loop
    while True:
        status(current_room, current_room_name, inventory)
        if 'Item' not in current_room.keys():
            command = input("Please enter which direction you want to go: ").capitalize()
        elif current_room['Item'] == 'Vampire':
            if len(inventory) != 6:
                print(f"\nThe Vampire has killed you.\nBetter luck next time!")
                break
            else:
                print(f"Congratulations, you killed the Vampire.\nPlease play again!")
                break
        else:
            command = input("Please enter if you want to pick up an item or which direction you want to go: ").capitalize()
        if command == 'Exit':
            print("\nThank you for playing Vampire Hunt")
            break
        elif command == 'Pickup':
            inventory.append(current_room['Item'])
            del current_room['Item']
        elif command in current_room.keys():
            current_room_name = current_room[command]
            current_room = rooms[current_room[command]]
        else:
            print(f"\nError.  Please enter a valid command.")
            continue

main()