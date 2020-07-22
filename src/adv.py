from room import Room
from player import Player
from item import Item


# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons,"),


    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Declare all the items

items = {
    'coins':   Item('coins', """Here are some small gold coins. Might be valuable."""),
    
    'hornets': Item('hornets', """Attack your enemy if needed with these"""),

    'key': Item('key', """Rusty old key lays here, Hopefully opens something."""),

    'hearts': Item('hearts', """Give a hug to yourself. Adds longevity and an extra life!"""),

} 

#link the items to rooms
room['outside'].items = [items['key']]
room['foyer'].items = [items['hearts']]
room['overlook'].items = [items['hornets']]
room['narrow'].items = [items['coins']]
room['treasure'].items = [items['hearts'], items['coins']]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Player_1", room["outside"])

# Write a loop that:
while True:
    player_1.current_room
    # * Prints the current room name
    print("\nYou are now in room:\n", player_1.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("Description:\n", player_1.current_room.description)

    available_items = []
    for item in player_1.current_room.items:
        available_items.append(item.name)
    if len(available_items)==0:
        print("\nItems in this room: None, you picked it up!")
    else:
        print("\nItems in this room:")
        for item in available_items:
            print(item)
            
# * Waits for user input and decides what to do.
    
    cmd = input("\nPress 'n', 's,', 'e', 'w' to move to a differnt room:\n \
Write 'take <insert item>' or drop <insert item>' to select item:\n \
Press 'i' to check inventory:\n \
or press 'q' to quit game:\n \
    ")


# If the user enters a cardinal direction, attempt to move to the room there.
    if len(cmd.split())==1:
        if cmd == 'n':
            print("\nWalking north...\n")
            if player_1.current_room.n_to is None:
                print("****There is no room to the North of you, select different direction.****")
            else:
                player_1.current_room = player_1.current_room.n_to
                
        elif cmd == 's':
            print("\nWalking south...\n")
            if player_1.current_room.s_to is None:
                print("****There is no room to the South of you. Select a different direction.****")
            else:
                player_1.current_room = player_1.current_room.s_to
        elif cmd == 'e':
            print("\nWalking east...\n")
            if player_1.current_room.e_to is None:
                print("****There is no room to the East of you. Select a different direction.****")
            else:
                player_1.current_room = player_1.current_room.e_to
        elif cmd == 'w':
            print("\nWalking west...\n")
            if player_1.current_room.w_to is None:
                print("****There is no room to the West of you. Select a different direction.****")
            else:
                player_1.current_room = player_1.current_room.w_to

# If the user enters "q", quit the game.
        elif cmd == 'q':
            print("Thanks for playing.  Have a nice day!")
            break

        if (cmd == 'i') | (cmd == "inventory"):
            print("Your inventory:")
            for item in player_1.inventory:
                print (item.name)    

# Print an error message if the movement isn't allowed.
        else:
            print ("This movement is not allowed.")

    elif len(cmd.split()) ==2:
        verb = cmd.split()[0]
        selected_item = cmd.split()[1]
        actions = ["take", "drop"]
        if verb in actions:
            if (verb == "take"):
                if selected_item in available_items:
                    player_1.add_item(items[selected_item])                    
                    items[selected_item].on_take()
                    available_items = player_1.current_room.remove_item(items[selected_item])
                else:
                    print("The item selected is not in this room")
            elif verb == "drop":
                inventory_items = []
                for item in player_1.inventory:
                    inventory_items.append(item.name)
                if selected_item in inventory_items:
                    player_1.current_room.add_item(items[selected_item])
                    player_1.remove_item(items[selected_item])
                    items[selected_item].on_drop()
                else:
                    print("The item is not in your inventory")


    
        







